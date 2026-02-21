import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailUtility:
    @staticmethod
    def send_email(smtp_server, port, sender_email, receiver_email, subject, body, username=None, password=None):
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                if username and password:
                    server.starttls()
                    server.login(username, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            return True
        except Exception as e:
            return str(e)
