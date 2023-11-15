""" Import models here so they auto-detect for makemigrations """
from api.addon_provider.models import AddonProvider
from api.authorized_storage_account.models import AuthorizedStorageAccount
from api.credentials.models import ExternalCredentials
from api.configured_storage_addon.models import ConfiguredStorageAddon
from api.external_account.models import ExternalAccount
from api.osf_resource.models import OSFResource
from api.osf_user.models import OSFUser
from api.storage_provider_settings.models import StorageProviderSettings

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
