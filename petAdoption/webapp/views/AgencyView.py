from django.http import HttpResponse
from ..managers.AgencyManager import AgencyManager
from rest_framework.decorators import api_view

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers.AgencySerializer import AgencySerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_agency(request):
    data = JSONParser().parse(request)
    agency = AgencyManager.create_agency(**data)
    serializer = AgencySerializer(agency)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_agency(request):
    data = JSONParser().parse(request)
    agency = AgencyManager.find_agency(data['agency_id'])
    serializer = AgencySerializer(agency)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_all_agencies(request):
    agencies = AgencyManager.find_all_agencies()
    serializer = AgencySerializer(agencies, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_agency(request):
    data = JSONParser().parse(request)
    AgencyManager.delete_agency(data['agency_id'])
    return HttpResponse('', content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_agency(request):
    data = JSONParser().parse(request)
    agency = AgencyManager.update_agency(**data)
    serializer = AgencySerializer(agency)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


