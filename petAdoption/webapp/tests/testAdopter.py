from django.test               import TestCase
from ..models.Adopter          import Adopter
from ..managers.AdopterManager import AdopterManager
from ..managers.AgencyManager  import AgencyManager
from ..managers.PetManager     import PetManager
from test_config               import *


class AdopterTestCase(TestCase):

    def setUp(self):
        adopter1 = AdopterManager.create_adopter(**sample_adopters[0])

        adopter2 = AdopterManager.create_adopter(**sample_adopters[1])

        agency = AgencyManager.create_agency(**sample_agencies[2])

        sample_pets[1]['agency_id'] = agency.id
        sample_pets[2]['agency_id'] = agency.id

        pet1 = PetManager.create_pet(**sample_pets[1])

        pet2 = PetManager.create_pet(**sample_pets[2])

        AdopterManager.set_favorite(adopter1.id, pet1.id)
        AdopterManager.set_favorite(adopter2.id, pet2.id)
        #AdopterManager.adopt_pet(adopter2.id)

    def test_create_adopter(self):
        adopter_count = Adopter.objects.all().count()
        self.assertEqual(adopter_count, 2)

    def test_set_favorite(self):
        adopters = Adopter.objects.all()
        self.assertEqual(adopters[0].favorite.pet_name, 'pet2')
        self.assertEqual(adopters[1].favorite.pet_name, 'pet3')

    # def test_adopt_pet(self):
    #     adopters = Adopter.objects.all()
    #     favorite_pet_1, adoption_succeed_1 = AdopterManager.adopt_pet(adopters[0].id)
    #     favorite_pet_2, adoption_succeed_2 = AdopterManager.adopt_pet(adopters[1].id)
    #     self.assertTrue(adoption_succeed_1)
    #     self.assertFalse(adoption_succeed_2)

    def test_delete_pet(self):
        pets = PetManager.find_all_pets()
        pet1_id = pets[0].id
        pet2_id = pets[1].id
        PetManager.delete_pet(pet1_id)
        PetManager.delete_pet(pet2_id)
        adopters = Adopter.objects.all()
        self.assertIsNone(adopters[0].favorite)
        self.assertIsNone(adopters[1].favorite)

    def test_delete_adopter(self):
        adopter1 = Adopter.objects.all()[0]
        AdopterManager.delete_adopter(adopter1.id)
        adopter_cnt = Adopter.objects.all().count()
        self.assertEqual(adopter_cnt, 1)








