from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel

class InternalUser(AddonsServiceBaseModel):
    user_uri = models.URLField(unique=True, db_index=True, null=False)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "Internal User"
        verbose_name_plural = "Internal Users"
        app_label = "addon_service"
