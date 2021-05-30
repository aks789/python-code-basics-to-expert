import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

M.login('email_id','app_password')

print(M.list())

print(M.select('inbox'))


typ,data = M.search(None, 'SUBJECT "Day "')

print(typ)
print(data)

res , email_data = M.fetch('email_id','(RFC822)')

raw_email = email_data[0][1]
print(raw_email)

raw_email_string = raw_email.decode('utf-8')
print(raw_email_string)

import email

email_message  = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type == 'text/html':
        body = part.get_payload(decode=True)
        print(body)




