from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel

class OSFResource(AddonsServiceBaseModel):
    resource_uri = models.URLField(unique=True, db_index=True, null=False)

    def __str__(self):
        return self.resource_uri

    class Meta:
        verbose_name = "OSF Resource"
        verbose_name_plural = "OSF Resources"
        app_label = "addon_service"
