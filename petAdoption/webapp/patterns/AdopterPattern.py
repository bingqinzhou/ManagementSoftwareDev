from django.conf.urls   import url
from ..views            import AdopterView


adopter_patterns = [

    url(r'^create',       AdopterView.create_adopter, name='create_adopter'),
    url(r'^delete',       AdopterView.delete_adopter, name='delete_adopter'),
    url(r'^find',         AdopterView.find_adopter, name='find_adopter'),
    url(r'^update',       AdopterView.update_adopter, name='update_adopter'),
    url(r'^all',          AdopterView.find_all_adopters, name='find_all_adopter'),
    url(r'^set_favorite', AdopterView.set_favorite, name='set_favorite'),
    url(r'^adopt_pet',    AdopterView.adopt_pet, name='adopt_pet')
]
