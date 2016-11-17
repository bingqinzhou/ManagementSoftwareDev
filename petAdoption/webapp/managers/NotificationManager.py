from EmailManager import EmailManager


class NotificationManager(object):

    @staticmethod
    def generate_email_config(related_adopters):
        to_email = []
        for adopter in related_adopters:
            to_email.append(adopter.email.encode('utf8'))
        email_config = {
            'from_email': 'PetAdoptionService@gmail.com',
            'to_email': to_email,
            'from_name': 'PetAdoption Service',
            'to_name': 'Related Adopters'
        }
        return email_config

    @staticmethod
    def send_notification(email_config, message_type):
        email_handler = EmailManager(**email_config)
        message = email_handler.get_msg_config()[message_type]
        email_handler.send_mail(message)

    @staticmethod
    def process_notification(related_adopters, message_type):
        email_config = NotificationManager.generate_email_config(related_adopters)
        NotificationManager.send_notification(email_config, message_type)

