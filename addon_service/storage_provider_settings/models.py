from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel


class StorageProviderSettings(AddonsServiceBaseModel):

    service_name = models.CharField()

    max_concurrent_downloads = models.IntegerField(null=False)
    max_upload_mb = models.IntegerField(null=False)

    auth_uri = models.URLField(null=False)

    provider = models.ForeignKey('addon_service.AddonProvider', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Storage Provider Settings"
        verbose_name_plural = "Storage Provider Settings"
        app_label = "addon_service"
