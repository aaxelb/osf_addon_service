""" Import models here so they auto-detect for makemigrations """
from addon_service.addon_provider.models import ExternalAddon
from addon_service.authorized_storage_account.models import AuthorizedStorageAccount
from addon_service.credentials.models import ExternalCredentials
from addon_service.configured_storage_addon.models import ConfiguredStorageAddon
from addon_service.external_account.models import ExternalAccount
from addon_service.internal_resource.models import InternalResource
from addon_service.internal_user.models import InternalUser
from addon_service.storage_provider_settings.models import StorageAddonSettings

__all__ = (
    'AuthorizedStorageAccount',
    # 'AuthorizedComputeAccount',
    'ConfiguredStorageAddon',
    # 'ConfiguredComputeAccount',
    'ExternalAccount',
    'ExternalAddon',
    'ExternalCredentials',
    'InternalResource',
    'InternalUser',
    'StorageAddonSettings'
    # 'ComputeAddonSettings',
)
