from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel

class OSFUser(AddonsServiceBaseModel):
    user_osf_uri = models.URLField(unique=True, db_index=True, null=False)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "OSF User"
        verbose_name_plural = "OSF Users"
        app_label = "addon_service"
