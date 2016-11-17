from rest_framework import serializers
from ..models import Question
from .AgencySerializer import AgencySerializer
from .AdopterSerializer import AdopterSerializer


class QuestionSerializer(serializers.ModelSerializer):

    agency = AgencySerializer()
    adopter = AdopterSerializer()

    class Meta:
        model = Question
        fields = ('id', 'title', 'content', 'answer', 'adopter', 'agency')