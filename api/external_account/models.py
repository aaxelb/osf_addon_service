from django.db import models

from api.utils.base_model import AddonsServiceBaseModel

class ExternalAccount(AddonsServiceBaseModel):

    # The user's ID on the remote service
    external_service_id = models.CharField()
    external_service_display_name = models.CharField()

    addon_provider = models.ForeignKey('api.AddonProvider', on_delete=models.CASCADE)
    owner = models.ForeignKey('api.OSFUser', on_delete=models.CASCADE)
    credentials = models.ForeignKey('api.ExternalCredentials', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "External Account"
        verbose_name_plural = "External Accounts"
        app_label = "api"
