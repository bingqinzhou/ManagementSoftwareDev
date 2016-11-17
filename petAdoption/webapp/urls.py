from django.conf.urls         import url, include
from patterns.AgencyPattern   import *
from patterns.PetPattern      import *
from patterns.AdopterPattern  import *
from patterns.QuestionPattern import *
from patterns.UserPattern     import *
from views                    import Index
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$',               Index.index, name='index'),
    url(r'^agencies/',       include(agency_patterns)),
    url(r'^pets/',           include(pet_patterns)),
    url(r'^adopters/',       include(adopter_patterns)),
    url(r'^questions/',      include(question_patterns)),
    url(r'^users/',          include(user_patterns)),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
