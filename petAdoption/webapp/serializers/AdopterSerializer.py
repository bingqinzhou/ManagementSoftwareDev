from rest_framework import serializers
from ..models import Adopter
from .PetSerializer import PetSerializer


class AdopterSerializer(serializers.ModelSerializer):

    favorite = PetSerializer()

    class Meta:
        model = Adopter
        fields = ('id', 'username', 'password', 'email', 'address',
                  'first_name', 'last_name', 'favorite')

