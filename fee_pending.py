import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def feepending(complete_data):
    for data in complete_data:
        smtp_server = "smtp.gmail.com"
        smtp_port=587

        username="kodudhulapoojitha19@gmail.com"
        password="uxxl hsok cklp ysla"

        from_email=username
        to_email=data[1]
        subject="Fee update"
        body=f"Dear {data[0]}, \nYou have fee pending \nPlease make sure to pay \nThank You"

        msg=MIMEMultipart()
        msg['From']=from_email
        msg['To']=to_email
        msg['Subject']=subject
        msg.attach(MIMEText(body,'plain'))

        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(username,password)
        server.send_message(msg)
        server.quit()

        #print(f"Mail sent to {data[0]}")
