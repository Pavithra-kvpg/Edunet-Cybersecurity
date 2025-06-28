from scapy.all import sniff, IP, TCP
import csv
import time
import yagmail

# Set up email alerts
EMAIL_ALERT = True
EMAIL_USER = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
TO_EMAIL = 'receiver_email@gmail.com'

yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

# Blacklisted IPs for demo
BLACKLISTED_IPS = ["192.168.1.10"]

def alert_user(message):
    print(f"[ALERT] {message}")
    if EMAIL_ALERT:
        yag.send(TO_EMAIL, subject="Intrusion Alert!", contents=message)

def log_packet(pkt, reason):
    with open("logs.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([time.ctime(), pkt[IP].src, pkt[IP].dst, pkt[IP].proto, reason])
    alert_user(f"Suspicious activity: {reason}\nSource: {pkt[IP].src}")

def detect_packet(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        proto = pkt[IP].proto

        if src_ip in BLACKLISTED_IPS:
            log_packet(pkt, "Blacklisted IP")

        if TCP in pkt:
            flags = pkt[TCP].flags
            if flags == "S":
                log_packet(pkt, "Possible port scan (SYN flood)")

print("[*] Starting IDS... Logging to logs.csv")
with open("logs.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Source IP", "Destination IP", "Protocol", "Alert Reason"])

sniff(prn=detect_packet, store=0)
