from ..models import Agency
from ..models import Pet
from ..models import Adopter
from ..managers.NotificationManager import NotificationManager


class PetManager(object):

    @staticmethod
    def create_pet(*args, **kwargs):
        agency = Agency.objects.get(id=kwargs['agency_id'])
        del kwargs['agency_id']
        kwargs['agency'] = agency
        new_pet = Pet.objects.create(**kwargs)
        new_pet.save()
        return new_pet

    @staticmethod
    def find_all_pets():
        return Pet.objects.all()

    @staticmethod
    def find_available_pets():
        return Pet.objects.filter(if_adopted=False)

    @staticmethod
    def find_pet(pet_id):
        return Pet.objects.get(id=pet_id)

    @staticmethod
    def delete_pet(pet_id):
        pet = Pet.objects.get(id=pet_id)
        pet.delete()

    @staticmethod
    def update_pet(*args, **kwargs):
        pet = Pet.objects.get(id=kwargs['pet_id'])
        if 'agency_id' in kwargs:
            agency = Agency.objects.get(id=kwargs['agency_id'])
            pet.agency = agency
        if 'pet_name' in kwargs:
            pet.pet_name = kwargs['pet_name']
        if 'if_adopted' in kwargs:
            pet.if_adopted = kwargs['if_adopted']
        if 'description' in kwargs:
            pet.description = kwargs['description']
        pet.save()
        related_adopters = PetManager.find_related_adopters(pet.id)
        NotificationManager.process_notification(related_adopters, 'pet_updated_message')
        return pet

    @staticmethod
    def find_related_adopters(pet_id):
        adopters = Adopter.objects.filter(favorite__id=pet_id)
        return adopters





