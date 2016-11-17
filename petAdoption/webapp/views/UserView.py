from django.http import HttpResponse
from rest_framework.decorators import api_view
from ..managers.UserManager import UserManager

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers.UserSerializer import UserSerializer


@api_view(['POST'])
def create_user(request):
    print('CREATE USER IS CALLED HERE!!!')
    data = JSONParser().parse(request)
    user = UserManager.create_user(data['username'], data['password'], data['email'])
    serializer = UserSerializer(user)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
def find_all_users(request):
    users = UserManager.find_all_users()
    serializer = UserSerializer(users, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


