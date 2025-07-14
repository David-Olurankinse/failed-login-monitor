#!/usr/bin/env python3

import re
from collections import defaultdict

LOG_FILE = "/var/log/auth.log"  # Adjust path if needed

def parse_failed_logins():
    failed_attempts = defaultdict(int)

    try:
        with open(LOG_FILE, "r") as f:
            for line in f:
                if "Failed password" in line:
                    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                    if match:
                        ip = match.group(1)
                        failed_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Log file {LOG_FILE} not found. Try running as sudo.")
        return

    print("Failed Login Attempts:")
    for ip, count in failed_attempts.items():
        print(f"{ip}: {count} times")

if __name__ == "__main__":
    parse_failed_logins()
