from ..models import Adopter
from ..models import Pet
from ..managers.NotificationManager import NotificationManager


class AdopterManager(object):

    @staticmethod
    def create_adopter(*args, **kwargs):
        new_adopter = Adopter.objects.create(**kwargs)
        new_adopter.save()
        return new_adopter

    @staticmethod
    def set_favorite(adopter_id, favorite_pet_id):
        adopter = Adopter.objects.get(id=adopter_id)
        favorite_pet = Pet.objects.get(id=favorite_pet_id)
        favorite_success = False
        if not favorite_pet.if_adopted:
            adopter.favorite = favorite_pet
            adopter.save()
            favorite_success = True
        return adopter, favorite_success

    @staticmethod
    def adopt_pet(adopter_id):
        adopter = Adopter.objects.get(id=adopter_id)
        favorite_pet = adopter.favorite
        adopt_success = False
        if not favorite_pet.if_adopted:
            favorite_pet.if_adopted = True
            favorite_pet.save()
            adopt_success = True
            related_adopters = AdopterManager.find_related_adopters(adopter_id)
            NotificationManager.process_notification(related_adopters, 'pet_adopted_message')
        return favorite_pet, adopt_success

    @staticmethod
    def find_related_adopters(adopter_id):
        adopter = Adopter.objects.get(id=adopter_id)
        similar_adopters = Adopter.objects.filter(favorite__id=adopter.favorite.id)\
            .exclude(id=adopter.id)
        return similar_adopters

    @staticmethod
    def find_adopter(adopter_id):
        return Adopter.objects.get(id=adopter_id)

    @staticmethod
    def find_all_adopters():
        return Adopter.objects.all()

    @staticmethod
    def delete_adopter(adopter_id):
        adopter = Adopter.objects.get(id=adopter_id)
        adopter.delete()

    @staticmethod
    def update_adopter(*args, **kwargs):
        adopter = Adopter.objects.get(id=kwargs['adopter_id'])
        if 'pet_id' in kwargs:
            pet = Pet.objects.get(id=kwargs['pet_id'])
            adopter.favorite = pet
        if 'username' in kwargs:
            adopter.username = kwargs['username']
        if 'password' in kwargs:
            adopter.password = kwargs['password']
        if 'email' in kwargs:
            adopter.email = kwargs['email']
        if 'address' in kwargs:
            adopter.address = kwargs['address']
        if 'first_name' in kwargs:
            adopter.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            adopter.last_name = kwargs['last_name']
        if 'favorite'  in kwargs:
            adopter.favorite = kwargs['favorite']
        adopter.save()
        return adopter


