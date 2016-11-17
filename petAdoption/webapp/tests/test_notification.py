from django.test               import TestCase
from ..models.Adopter          import Adopter
from ..managers.AdopterManager import AdopterManager
from ..managers.AgencyManager  import AgencyManager
from ..managers.PetManager     import PetManager
from test_config               import *


class NotificationTestCase(TestCase):

    def setUp(self):
        agency = AgencyManager.create_agency(**sample_agencies[2])
        sample_pets[2]['agency_id'] = agency.id
        pet = PetManager.create_pet(**sample_pets[2])
        adopter1 = AdopterManager.create_adopter(**sample_email_adopters[0])
        adopter2 = AdopterManager.create_adopter(**sample_email_adopters[1])
        adopter3 = AdopterManager.create_adopter(**sample_email_adopters[2])
        AdopterManager.set_favorite(adopter1.id, pet.id)
        AdopterManager.set_favorite(adopter2.id, pet.id)
        AdopterManager.set_favorite(adopter3.id, pet.id)

    def test_adopt_pet(self):
        adopter = Adopter.objects.all()[2]
        AdopterManager.adopt_pet(adopter.id)