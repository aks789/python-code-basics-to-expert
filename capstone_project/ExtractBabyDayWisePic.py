import imaplib
import email


M = imaplib.IMAP4_SSL('imap.gmail.com',993)

M.login('gmail_id','app_password')

print(M.list())

M.select('"[Gmail]/Sent Mail"')
result, data = M.search(None, 'SUBJECT "DAY "')

for email_data in data[0].split():
    rv, mail_day_data = M.fetch(email_data,'(RFC822)')
    raw_email = mail_day_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    decoded_header = email.header.make_header(email.header.decode_header(email_message['Subject']))
    print('Subject is: ' + str(decoded_header))
    day_wise_num =  str(decoded_header)
    for part in email_message.walk():
        if part.get_content_maintype()=='image':
            file = open('D:\\baby_vera\\extract_vera_images_daywise' + '/' + day_wise_num + '.jpeg', 'wb')\
                .write(part.get_payload(decode=True))



