from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel


class ExternalAddon(AddonsServiceBaseModel):

    provider_name = models.CharField(null=False)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "Addon Provider"
        verbose_name_plural = "Addon Providers"
        app_label = "addon_service"
