from django.http import HttpResponse
from rest_framework.decorators import api_view
from ..managers.QuestionManager import QuestionManager

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..serializers.QuestionSerializer import QuestionSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def create_question(request):
    data = JSONParser().parse(request)
    question = QuestionManager.create_question(**data)
    serializer = QuestionSerializer(question)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def answer_question(request):
    data = JSONParser().parse(request)
    question = QuestionManager.answer_question(data['question_id'], data['answer'])
    serializer = QuestionSerializer(question)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_question(request):
    data = JSONParser().parse(request)
    question = QuestionManager.find_question(data['question_id'])
    serializer = QuestionSerializer(question)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def find_all_questions(request):
    questions = QuestionManager.find_all_questions()
    serializer = QuestionSerializer(questions, many=True)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def delete_question(request):
    data = JSONParser().parse(request)
    QuestionManager.delete_question(data['question_id'])
    return HttpResponse('', content_type="application/json")


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_question(request):
    data = JSONParser().parse(request)
    question = QuestionManager.update_question(**data)
    serializer = QuestionSerializer(question)
    content = JSONRenderer().render(serializer.data)
    return HttpResponse(content, content_type="application/json")



