from django.test               import TestCase
from ..models.Pet              import Pet
from ..managers.PetManager     import PetManager
from ..managers.AgencyManager  import AgencyManager
from test_config               import *

class PetTestCase(TestCase):

    def setUp(self):
        agency = AgencyManager.create_agency(**sample_agencies[1])
        sample_pets[0]['agency_id'] = agency.id
        sample_pets[1]['agency_id'] = agency.id
        pet1 = PetManager.create_pet(**sample_pets[0])
        pet2 = PetManager.create_pet(**sample_pets[1])
        pet2.if_adopted = True

    def test_create_pet(self):
        pet_count = Pet.objects.all().count()
        self.assertEqual(pet_count, 2)

    def test_find_all_pets(self):
        pets = PetManager.find_all_pets()
        self.assertEqual(pets[0].pet_name, 'pet1')
        self.assertEqual(pets[1].pet_name, 'pet2')
        self.assertEqual(pets[0].agency.username, 'user5')

    def find_available_pets(self):
        available_pets = PetManager.find_available_pets()
        self.assertEqual(available_pets.count(), 1)
        self.assertEqual(available_pets[0].pet_name, 'pet1')





