from django.db import models

from api.utils.base_model import AddonsServiceBaseModel

class StorageProviderSettings(AddonsServiceBaseModel):

    service_name = models.CharField()

    read_only = models.BooleanField(null=False)

    #TODO: consider replacing this with an array of supported_operations and a backing enum?
    # Can copy data *into* accounts on this provider
    supports_copy = models.BooleanField(null=False)
    # Root folder is configurable on a per-project basis
    supports_user_specified_root_folder = models.BooleanField(null=False)
    # Can select/create specific versions of a file
    supports_file_versioning = models.BooleanField(null=False)
    # Can download all data in a zip
    supports_bulk_download = models.BooleanField(null=False)

    max_concurrent_downloads = models.IntegerField(null=False)
    max_upload_mb = models.IntegerField(null=False)

    auth_uri = models.URLField(null=False)

    provider = models.ForeignKey('api.AddonProvider', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Storage Provider Settings"
        verbose_name_plural = "Storage Provider Settings"
        app_label = "api"
