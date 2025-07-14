# Failed Login Monitor

A simple Python script that monitors failed SSH login attempts from system logs and reports repeated failures. Great for detecting brute-force attacks or probing activity on Linux systems.

## Features

- Scans `/var/log/auth.log` (or `/var/log/secure`) for failed login entries
- Extracts and counts failed attempts by IP address
- Prints a summary to the console

## Requirements

- Python 3.x
- Linux system (Ubuntu/Debian/CentOS)
- `sudo` access to read system logs

## Usage

```bash
sudo python3 monitor.py


Sample output:


Failed Login Attempts:
192.168.1.45: 4 times
203.0.113.88: 2 times


Author

**David Olurankinse**  
[LinkedIn](https://www.linkedin.com/in/david-olurankinse-98210122b)  
[GitHub](https://github.com/David-Olurankinse)  
Email: dolufelix@gmail.com  