from django.test                    import TestCase
from ..models.Question              import Question
from ..managers.QuestionManager     import QuestionManager
from ..managers.AgencyManager       import AgencyManager
from ..managers.AdopterManager      import AdopterManager
from test_config                    import *


class PetTestCase(TestCase):

    def setUp(self):
        agency = AgencyManager.create_agency(**sample_agencies[0])
        adopter = AdopterManager.create_adopter(**sample_adopters[0])
        sample_questions[0]['agency_id'] = agency.id
        sample_questions[0]['adopter_id'] = adopter.id
        question = QuestionManager.create_question(**sample_questions[0])

        QuestionManager.answer_question(question.id, sample_answers[0])

    def test_create_question(self):
        question_count = Question.objects.all().count()
        self.assertEqual(question_count, 1)

    def tests_anwer_question(self):
        question = Question.objects.all()[0]
        self.assertEqual(question.answer, sample_answers[0])

    def test_delete_questions(self):
        question = Question.objects.all()[0]
        QuestionManager.delete_question(question.id)
        question_cnt = Question.objects.all().count()
        self.assertEqual(question_cnt, 0)

