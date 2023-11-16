from factory.django import DjangoModelFactory
from addon_service.osf_user.models import OSFUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = OSFUser
