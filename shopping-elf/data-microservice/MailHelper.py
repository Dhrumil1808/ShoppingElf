import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText




def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              smtpserver='smtp.gmail.com:587'):

    # Prepare actual message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login("shoppingelf.3clicks@gmail.com", "Testpwd@123")
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr_list[0]
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    problems = server.sendmail(from_addr, to_addr_list, msg.as_string())
    server.quit()



def testMail():
    sendemail(from_addr='shoppingelf.3clicks@gmail.com',
              to_addr_list=['rashmishrm74@gmail.com'],
              cc_addr_list=[],
              subject='Shopping List',
              message='Here is your Shopping List',
             )


#testMail()

