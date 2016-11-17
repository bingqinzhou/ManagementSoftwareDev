from rest_framework import serializers
from ..models import Agency


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ('id', 'username', 'password', 'email', 'address', 'company_name')