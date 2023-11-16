from django.db import models

from addon_service.utils.base_model import AddonsServiceBaseModel

class ExternalAccount(AddonsServiceBaseModel):

    # The user's ID on the remote service
    external_service_id = models.CharField()
    external_service_display_name = models.CharField()

    addon_provider = models.ForeignKey('addon_service.ExternalAddon', on_delete=models.CASCADE)
    owner = models.ForeignKey('addon_service.InternalUser', on_delete=models.CASCADE)
    credentials = models.ForeignKey('addon_service.ExternalCredentials', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "External Account"
        verbose_name_plural = "External Accounts"
        app_label = "addon_service"
