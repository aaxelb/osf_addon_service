from django.db import models

from api.utils.base_model import AddonsServiceBaseModel

class ConfiguredStorageAddon(AddonsServiceBaseModel):

    root_folder = models.CharField()

    external_account = models.ForeignKey('api.ExternalAccount', on_delete=models.CASCADE)
    osf_resource = models.ForeignKey('api.OSFResource', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "Configured Storage Addon"
        verbose_name_plural = "Configured Storage Addons"
        app_label = "api"
