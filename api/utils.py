import smtplib
from email.mime.text import MIMEText

def send_alert_email(message: str):
    """
    TODO: Configure email username, password, receiver in .env
    This function already sends the email.
    """

    msg = MIMEText(message)
    msg["Subject"] = "KT Exam Alert"
    msg["From"] = "YOUR_EMAIL"
    msg["To"] = "RECEIVER_EMAIL"

    try:
        # Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # TODO: Login using secure credentials from environment variables
        server.login("YOUR_EMAIL", "YOUR_PASSWORD")

        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Email sending failed:", e)
