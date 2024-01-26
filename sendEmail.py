import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import re
import socket

SYSTEM_EMAIL = "Attendance.NU@gmail.com"
PASSWORD = "dyftxileardalgvi"
SMTP_PORT = 587                 # Standard secure SMTP port
SMTP_SERVER = "smtp.gmail.com"  # Google SMTP_SERVER

def send_endEmail(DR_EMAIL, COURSE_CODE, FILE_PATH):

    body = f"""
    Dear Professor {DR_EMAIL.split("@")[0]},
    We hope this email finds you safe.

    Upon your request, we're glad to inform you that the attendance for the lecture {COURSE_CODE} is attached it with this email.

    Thanks
    """
    msg = MIMEMultipart()
    msg['From'] = SYSTEM_EMAIL
    msg['To'] = DR_EMAIL
    msg['Subject'] = f"Attendance for {COURSE_CODE} is here!"

    msg.attach(MIMEText(body, 'plain'))


    attachment= open(FILE_PATH, 'rb')

    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', "attachment; filename= " + FILE_PATH)
    msg.attach(attachment_package)

    text = msg.as_string()

    TIE_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    TIE_server.starttls()
    TIE_server.login(SYSTEM_EMAIL, PASSWORD)
    TIE_server.sendmail(SYSTEM_EMAIL, DR_EMAIL, text)
    TIE_server.quit()

def send_startEmail(DR_EMAIL, COURSE_CODE, OTP_PASSCODE):

    body = f"""
    Dear Professor {DR_EMAIL.split("@")[0]},
    We hope this email finds you safe.

    Upon your request, we're glad to inform you that the Automatic attendance section for the lecture {COURSE_CODE} is currently running.
    plseae use this OTP: {OTP_PASSCODE} to end you section and download you attendance Excel file http://127.0.0.1:5000/endSession

    Thanks
    """
    msg = MIMEMultipart()
    msg['From'] = SYSTEM_EMAIL
    msg['To'] = DR_EMAIL
    msg['Subject'] = f"OTP for {COURSE_CODE} attendance!"

    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    TIE_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    TIE_server.starttls()
    TIE_server.login(SYSTEM_EMAIL, PASSWORD)
    TIE_server.sendmail(SYSTEM_EMAIL, DR_EMAIL, text)
    TIE_server.quit()

def checkEmail(email):
    gmail_regex = r"^[a-zA-Z0-9.]+@gmail\.com$"
    return bool(re.match(gmail_regex, email))

def is_internet_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        return False