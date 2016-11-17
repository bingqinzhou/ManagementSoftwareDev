from django.test               import TestCase
from ..models.Agency           import Agency
from ..managers.AgencyManager  import AgencyManager

from test_config import *


class AgencyTestCase(TestCase):

    def setUp(self):
        AgencyManager.create_agency(**sample_agencies[0])

    def test_create_agency(self):
        agencies_count = Agency.objects.all().count()
        self.assertEqual(agencies_count, 1)
        agency = Agency.objects.all()[0]
        self.assertEqual(agency.username, 'user4')


    def test_delete_agency(self):
        agency = Agency.objects.all()[0]
        AgencyManager.delete_agency(agency.id)
        agencies_count = Agency.objects.all().count()
        self.assertEqual(agencies_count, 0)



