from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

import smtplib, ssl

from email import encoders

port = 587

server = "smtp-mail.outlook.com"

sender = "example@outlook.com"

recipient = "example@gmail.com"

password = "strongpassword"

msg = MIMEMultipart()       

message = "This email includes an attachment"

msg.attach(MIMEText(message, "plain"))

filename = "example.pdf"

with open(filename, "rb") as pdf:

    attachment = MIMEBase("application", "octet-stream")

    attachment.set_payload(pdf.read())

encoders.encode_base64(attachment)

attachment.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

msg.attach(attachment)


SSLcontext = ssl.create_default_context()

with smtplib.SMTP("mail.redrosecarehomes.com", 587) as server:

    server.starttls(context=SSLcontext)

    server.login(sender, password)

    server.sendmail(sender, recipient, msg.as_string())
    
    print(1+1)