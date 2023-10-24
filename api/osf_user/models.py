from django.db import models


class OSFUser(models.Model):
    user_guid = models.CharField(max_length=100, unique=True, primary_key=True)

    def __str__(self):
        return self.user_guid

    class Meta:
        verbose_name = "OSF User"
        verbose_name_plural = "OSF Users"
        app_label = "api"
