from django.conf.urls   import url
from ..views            import PetView


pet_patterns = [
    url(r'^create',    PetView.create_pet, name='create_pet'),
    url(r'^find',      PetView.find_pet, name='find_pet'),
    url(r'^delete',    PetView.delete_pet, name='delete_pet'),
    url(r'^update',    PetView.update_pet, name='update_pet'),
    url(r'^all',       PetView.find_all_pets, name='find_all_pets'),
    url(r'^available', PetView.find_available_pets, name='find_available_pets'),
]

