from django.test                import TestCase
from django.contrib.auth.models import User
from ..managers.UserManager     import UserManager


class UserTestCase(TestCase):

    def setUp(self):
        UserManager.create_user('api_user1', '1234', 'api_user1@gmail.com')
        UserManager.create_user('api_user2', '1234', 'api_user2@gmail.com')

    def test_create_pet(self):
        user_cnt = User.objects.all().count()
        self.assertEqual(user_cnt, 2)

    def test_find_all_users(self):
        users = UserManager.find_all_users()
        self.assertEqual(users[0].username, 'api_user1')
        self.assertEqual(users[1].username, 'api_user2')
