import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = "eProfileassiotwomennhealthVRF@outlook.com"
    msg['To'] = to_email
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))

    try:

        s = smtplib.SMTP("smtp.office365.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()

        s.login('eProfileassiotwomennhealthVRF@outlook.com',
                '14789632150*Eprofile#')

        s.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        s.quit()
