# 🔐 Failed Login Monitor

A simple Python script that monitors failed SSH login attempts from system logs and reports repeated failures. Great for detecting brute-force attacks or probing activity on Linux systems.

---

## 📌 Features

- Scans `/var/log/auth.log` (or `/var/log/secure`) for failed login entries
- Extracts and counts failed attempts by IP address
- Prints a summary to the console

---

## ⚙️ Requirements

- Python 3.x
- Linux system (Ubuntu/Debian/CentOS)
- `sudo` access to read system logs

---

## 🚀 Usage

```bash
sudo python3 monitor.py
