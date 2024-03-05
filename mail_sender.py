from email.message import EmailMessage
import ssl
import smtplib


def mail_sender():
    
    email_sender = "beratbayraktar381@gmail.com"
    password = "gvduiyiqfsmwdarn"
    mail = "beratbayraktar374@gmail.com"
    email_rec = "{}".format(mail)

    body = """
       Adatepe, Erdem Cd., 35400 Buca/İzmirr
    
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_rec
    em['Subject'] = "Email Subject"
    em.set_content (body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_rec,em.as_string())

    
mail_sender()