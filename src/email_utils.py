"""
Email notification utility for enterprise-api-test-framework
"""
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port=587, username=None, password=None):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        if username and password:
            server.login(username, password)
        server.sendmail(from_email, [to_email], msg.as_string())
