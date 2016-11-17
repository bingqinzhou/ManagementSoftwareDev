from rest_framework import serializers
from ..models import Pet
from .AgencySerializer import AgencySerializer


class PetSerializer(serializers.ModelSerializer):

    agency = AgencySerializer()

    class Meta:
        model = Pet
        fields = ('id', 'pet_name', 'if_adopted', 'description', 'agency')