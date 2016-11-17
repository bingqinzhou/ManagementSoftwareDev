from django.http import HttpResponse
from rest_framework.decorators import api_view
from ..managers.AdopterManager import AdopterManager

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers.AdopterSerializer import AdopterSerializer
from ..serializers.PetSerializer import PetSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_adopter(request):
    data = JSONParser().parse(request)
    adopter = AdopterManager.create_adopter(**data)
    serializer = AdopterSerializer(adopter)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def set_favorite(request):
    data = JSONParser().parse(request)
    adopter, favorite_success = AdopterManager.set_favorite(data['adopter_id'], data['favorite_pet_id'])
    serializer = AdopterSerializer(adopter)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def adopt_pet(request):
    data = JSONParser().parse(request)
    favorite_pet, adoption_succeed = AdopterManager.adopt_pet(data['adopter_id'])
    serializer = PetSerializer(favorite_pet)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_adopter(request):
    data = JSONParser().parse(request)
    adopter = AdopterManager.find_adopter(data['adopter_id'])
    serializer = AdopterSerializer(adopter)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_all_adopters(request):
    adopters = AdopterManager.find_all_adopters()
    serializer = AdopterSerializer(adopters, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_adopter(request):
    data = JSONParser().parse(request)
    AdopterManager.delete_adopter(data['adopter_id'])
    return HttpResponse('', content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_adopter(request):
    data = JSONParser().parse(request)
    adopter = AdopterManager.update_adopter(**data)
    serializer = AdopterSerializer(adopter)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")
