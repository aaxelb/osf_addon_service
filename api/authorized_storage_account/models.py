from django.contrib.postgres.fields import ArrayField
from django.db import models

from api.utils.base_model import AddonsServiceBaseModel

class AuthorizedStorageAccount(AddonsServiceBaseModel):

    scopes = ArrayField(models.CharField(max_length=128), default=list, blank=True)
    default_root_folder = models.CharField()

    base_account = models.ForeignKey('api.ExternalAccount', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Authorized Storage Account"
        verbose_name_plural = "Authorized Storage Accounts"
        app_label = "api"
