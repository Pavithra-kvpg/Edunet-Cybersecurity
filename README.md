# EDUNET CYBERSECURITY 

# 🛡️ Intrusion Detection System (IDS) using Python

This project implements a lightweight Intrusion Detection System (IDS) using Python. It monitors live network traffic, detects suspicious activities like port scans and blacklisted IP access, logs events, and sends real-time email alerts. A user-friendly Streamlit dashboard is included to visualize and filter alerts.

---

## 🚀 Features

- ✅ Live packet sniffing using `scapy`
- ✅ Rule-based detection for:
  - Blacklisted IP access
  - Port scanning via SYN flood detection
- ✅ Real-time email alerts using `yagmail`
- ✅ Logs suspicious activity to CSV file
- ✅ Streamlit dashboard to view and filter alerts interactively


## 🛠️ Technologies Used

- Python 3.x
- Scapy – packet sniffing
- Yagmail – email alerts
- Streamlit – GUI dashboard
- CSV – log storage


## ⚙️ Installation

1. **Clone the repository**

git clone https://github.com/your-username/Intrusion-Detection-System.git
cd Intrusion-Detection-System

2. Install required packages

pip install -r 
requirements.txt

## 🔐 Email Alert Setup

Edit the ids.py file with your credentials:

EMAIL_USER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
TO_EMAIL = 'receiver_email@gmail.com'

## Steps:

Enable 2FA in your Gmail account

Visit https://myaccount.google.com/apppasswords

Generate an app-specific password and use it in the code

## ▶️ How to Run

1. Start the IDS

sudo python ids.py

> Starts packet sniffing and logs alerts to logs.csv.



2. Launch the Dashboard

streamlit run ids_gui.py

> Opens a web dashboard for live monitoring.

## 📊 Sample Log Format

Time	Source IP	Destination IP	Protocol	Alert Reason

Sat Jun 28 13:00:22	192.168.1.10	192.168.1.5	6 (TCP)	Blacklisted IP
Sat Jun 28 13:05:30	192.168.1.11	192.168.1.5	6 (TCP)	Possible port scan (SYN)*
