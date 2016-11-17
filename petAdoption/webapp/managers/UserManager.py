from django.contrib.auth.models import User


class UserManager(object):

    @staticmethod
    def find_all_users():
        return User.objects.all()

    @staticmethod
    def create_user(_username, _password, _email):
        new_user = User.objects.create_user(username=_username, password=_password, email=_email)
        return new_user






