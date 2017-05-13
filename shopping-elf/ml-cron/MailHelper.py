import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s' % from_addr
    header += 'To: %s' % ', '.join(to_addr_list)
    header += 'Cc: %s' % ', '.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = +message
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()



def testMail():
    sendemail(from_addr='shoppingelf.3clicks@gmail.com',
              to_addr_list=['rashmishrm74@gmail.com'],
              cc_addr_list=[],
              subject='Howdy',
              message='Howdy from a python function',
              login='shoppingelf.3clicks@gmail.com',
              password='Testpwd@123')


testMail()

