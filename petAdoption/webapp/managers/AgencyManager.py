from ..models import Agency


class AgencyManager(object):

    @staticmethod
    def create_agency(*args, **kwargs):
        new_agency = Agency.objects.create(**kwargs)
        new_agency.save()
        return new_agency

    @staticmethod
    def find_all_agencies():
        return Agency.objects.all()

    @staticmethod
    def find_agency(agency_id):
        return Agency.objects.get(id=agency_id)

    @staticmethod
    def delete_agency(agency_id):
        agency = Agency.objects.get(id=agency_id)
        agency.delete()

    @staticmethod
    def update_agency(*args, **kwargs):
        agency = Agency.objects.get(id=kwargs['agency_id'])
        if 'username' in kwargs:
            agency.username = kwargs['username']
        if 'password' in kwargs:
            agency.password = kwargs['password']
        if 'email' in kwargs:
            agency.email = kwargs['email']
        if 'address' in kwargs:
            agency.address = kwargs['address']
        if 'company_name' in kwargs:
            agency.company_name = kwargs['company_name']
        agency.save()
        return agency


