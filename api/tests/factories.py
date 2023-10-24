from factory.django import DjangoModelFactory
from api.osf_user.models import OSFUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = OSFUser
