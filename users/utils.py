import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = "wpbawomenhealth@outlook.com"
    msg['To'] = to_email
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))

    try:

        s = smtplib.SMTP("smtp.office365.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()

        s.login('wpbawomenhealth@outlook.com', '15973*Womenhealth')

        s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        s.quit()
