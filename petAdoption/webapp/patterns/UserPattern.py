from django.conf.urls   import url
from ..views            import UserView


user_patterns = [

    url(r'^create', UserView.create_user, name='create_user'),
    url(r'^all',    UserView.find_all_users, name='find_all_users')
]