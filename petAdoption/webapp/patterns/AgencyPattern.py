from django.conf.urls   import url
from ..views            import AgencyView


agency_patterns = [

    url(r'^create', AgencyView.create_agency, name='create_agency'),
    url(r'^delete', AgencyView.delete_agency, name='delete_agency'),
    url(r'^update', AgencyView.update_agency, name='update_agency'),
    url(r'^find',   AgencyView.find_agency, name='find_agency'),
    url(r'^all',    AgencyView.find_all_agencies, name='find_all_agencies')

]
