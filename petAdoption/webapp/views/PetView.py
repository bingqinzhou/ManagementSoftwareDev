from django.http import HttpResponse
from rest_framework.decorators import api_view
from ..managers.PetManager import PetManager

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers.PetSerializer import PetSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_pet(request):
    data = JSONParser().parse(request)
    pet = PetManager.create_pet(**data)
    serializer = PetSerializer(pet)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_all_pets(request):
    pets = PetManager.find_all_pets()
    serializer = PetSerializer(pets, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_available_pets(request):
    available_pets = PetManager.find_available_pets()
    serializer = PetSerializer(available_pets, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_pet(request):
    data = JSONParser().parse(request)
    pet = PetManager.find_pet(data['pet_id'])
    serializer = PetSerializer(pet)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_pet(request):
    data = JSONParser().parse(request)
    PetManager.delete_pet(data['pet_id'])
    return HttpResponse('', content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_pet(request):
    data = JSONParser().parse(request)
    pet = PetManager.update_pet(**data)
    serializer = PetSerializer(pet)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")

