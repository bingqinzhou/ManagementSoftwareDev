from django.conf.urls   import url
from ..views            import QuestionView


question_patterns = [

    url(r'^create', QuestionView.create_question, name='create_question'),
    url(r'^find',   QuestionView.find_question, name='find_question'),
    url(r'^delete', QuestionView.delete_question, name='delete_question'),
    url(r'^update', QuestionView.update_question, name='update_question'),
    url(r'^all',    QuestionView.find_all_questions, name='find_all_questions'),
    url(r'^answer', QuestionView.answer_question, name='answer_question')
]