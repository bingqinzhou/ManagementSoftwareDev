from ..models import Question
from ..models import Agency
from ..models import Adopter


class QuestionManager(object):

    @staticmethod
    def create_question(*args, **kwargs):
        adopter = Adopter.objects.get(id=kwargs['adopter_id'])
        agency = Agency.objects.get(id=kwargs['agency_id'])
        del kwargs['adopter_id']
        del kwargs['agency_id']
        kwargs['adopter'] = adopter
        kwargs['agency'] = agency
        new_question = Question.objects.create(**kwargs)
        new_question.save()
        return new_question

    @staticmethod
    def answer_question(question_id, _answer):
        question = Question.objects.get(id=question_id)
        question.answer = _answer
        question.save()
        return question

    @staticmethod
    def find_question(question_id):
        return Question.objects.get(id=question_id)

    @staticmethod
    def find_all_questions():
        return Question.objects.all()

    @staticmethod
    def delete_question(question_id):
        question = Question.objects.get(id=question_id)
        question.delete()

    @staticmethod
    def update_question(*args, **kwargs):
        question = Question.objects.get(id=kwargs['question_id'])
        if 'adopter_id' in kwargs:
            adopter = Adopter.objects.get(id=kwargs['adopter_id'])
            question.adopter = adopter
        if 'agency_id' in kwargs:
            agency = Agency.objects.get(id=kwargs['agency_id'])
            question.agency = agency
        if 'title' in kwargs:
            question.title = kwargs['title']
        if 'content' in kwargs:
            question.content = kwargs['content']
        if 'answer' in kwargs:
            question.answer = kwargs['answer']
        question.save()
        return question
