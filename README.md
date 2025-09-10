# KEYLOGGER-DAEMON
A simple daemon that logs keyboard inputs to a database for personal/local use.

## 📋 Предварительные требования
- Python 3.13.5
- Linux (Debian/Ubuntu/Arch)
- sqlite3
- Systemd
- virtualenv

## 🚀 Setup and installation

1. Clone repository
```
git clone git@github.com:prpanz/keylogger-daemon.git
cd keylogger-daemon
```
2. Creating a virtual environment and installing dependencies
```
python -m venv venv
source /venv/bin/activate
pip install -r requirements.txt
```
3. Setup a systemd service
```
sudo nano /etc/systemd/system/keylogger.service
```
```
[Unit]  
Description=Keylogger Daemon  
After=network.target

[Service]
Type=simple  
User=root  
Environment=PATH_TO_DB=/var/lib/keylogger/data.db  
Environment=TABLE_NAME=keylogs  
WorkingDirectory=/path/to/working_directory  
ExecStart=/path/to/venv/bin/python /path/to/keylogger.py  
Restart=always  

[Install]  
WantedBy=multi-user.target  
```
5. Run service
```
sudo systemctl daemon-reload
sudo systemctl start keylogger
sudo systemctl enable keylogger
```
6. Check daemon status || logs
```
sudo systemctl status keylogger
sudo journalctl -u keylogger -n 50
```

---
*This project is for educational and personal purposes. Use responsibly.*