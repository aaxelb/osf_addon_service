from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel


class ExternalAddon(AddonsServiceBaseModel):

    name = models.CharField(null=False)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "External Addon"
        verbose_name_plural = "External Addons"
        app_label = "addon_service"
