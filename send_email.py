import smtplib
import logging
import sys


from config.config import EmailConfig

EmailConfig.read_from_file()

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

logHandler = logging.StreamHandler(sys.stdout)
# logHandler.setLevel(logging.DEBUG)

# create a logging format
logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s- %(message)s'
)


def send_email(subject: str, msg: str) -> None:
    try:
        server = smtplib.SMTP(EmailConfig.HOST+':'+EmailConfig.PORT)

        server.ehlo()
        server.starttls()
        server.login(EmailConfig.SENDER_EMAIL_ADDRESS, EmailConfig.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EmailConfig.SENDER_EMAIL_ADDRESS, EmailConfig.RECIPIENT_EMAIL_ADDRESS, message)
        server.quit()
        logger.info("Success: Email sent!")
    except:
        logger.critical("Email failed to send")
