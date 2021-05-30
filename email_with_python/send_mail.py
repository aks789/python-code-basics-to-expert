import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

print(smtp_object.ehlo())

smtp_object.starttls()

#email = getpass.getpass('Email : ')
#password = getpass.getpass('Password Please: ')

print(smtp_object.login('email_id','app_password'))

from_addr = ''
to_addr = ''
subject = input("enter subject line: ")
message = input("Enter the message : ")
msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_addr,to_addr,msg)

smtp_object.quit()

