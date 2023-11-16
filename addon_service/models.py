""" Import models here so they auto-detect for makemigrations """
from addon_service.addon_provider.models import AddonProvider
from addon_service.authorized_storage_account.models import AuthorizedStorageAccount
from addon_service.credentials.models import ExternalCredentials
from addon_service.configured_storage_addon.models import ConfiguredStorageAddon
from addon_service.external_account.models import ExternalAccount
from addon_service.osf_resource.models import OSFResource
from addon_service.osf_user.models import OSFUser
from addon_service.storage_provider_settings.models import StorageProviderSettings

__all__ = (
    'AddonProvider',
    'AuthorizedStorageAccount',
    'ExternalCredentials',
    'ConfiguredStorageAddon',
    'ExternalAccount',
    'OSFResource',
    'OSFUser',
    'StorageProviderSettings'
)
