import smtplib
from email.mime.text import MIMEText
from email.header    import Header


message1 = MIMEText('Dear Adopter,\r\n\r\nWe are sorry to inform you '
                    'that your favorite has just been adopted :(\r\n\r\nSincerely,\r\nPetAdoption Service',
                    'plain', 'utf-8')
message1['Subject'] = 'Your favorite pet is adopted!'

message2 = MIMEText('Dear Adopter,\r\n\r\nThis email to inform you that the information of your favorite'
                    'pet has just been updated :D\r\n\r\nSincerely,\r\nPetAdoption Service',
                    'plain', 'utf-8')
message2['Subject'] = 'The information of your favorite pet has been updated!'

msg_config = {

    'pet_adopted_message': message1,
    'pet_updated_message': message2
}


class EmailManager(object):

    def __init__(self, **kwargs):
        self.from_email = kwargs['from_email']
        self.to_email = kwargs['to_email']
        self.from_name = kwargs['from_name']
        self.to_name = kwargs['to_name']

    def send_mail(self, message):
        try:
            message['From'] = Header(self.from_name, 'utf-8')
            message['To'] = Header(self.to_name, 'utf-8')
            smtp_sock = smtplib.SMTP("smtp.gmail.com", 587)
            gmail_user = 'PetAdoptionService@gmail.com '
            gmail_pwd = 'neucs5500'
            smtp_sock.starttls()
            smtp_sock.ehlo()
            smtp_sock.login(gmail_user, gmail_pwd)
            smtp_sock.sendmail(self.from_email, self.to_email, message.as_string())
            print "Email sent successfully"
        except smtplib.SMTPException:
            print "Error: Unable to Send Email"

    def get_msg_config(self):
        return msg_config



