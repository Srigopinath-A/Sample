import smtplib
from email.mime.text import MIMEText

def send_email():
    msg = MIMEText("This is a test email sent from AWX using a Python script.")
    msg["Subject"] = "Test Email from AWX"
    msg["From"] = "your-email@example.com"
    msg["To"] = "recipient@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_smtp_username", "your_smtp_password")
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
