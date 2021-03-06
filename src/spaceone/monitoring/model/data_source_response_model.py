from schematics.models import Model
from schematics.types import ListType, DictType, StringType
from schematics.types.compound import ModelType

__all__ = ['PluginVerifyResponseModel']

_SUPPORTED_RESOURCE_TYPE = [
    'inventory.Server',
    'inventory.CloudService'
]


class ReferenceKeyModel(Model):
    resource_type = StringType(required=True, choices=_SUPPORTED_RESOURCE_TYPE)
    reference_key = StringType(required=True)


class PluginOptionsModel(Model):
    supported_resource_type = ListType(StringType, default=_SUPPORTED_RESOURCE_TYPE)
    reference_keys = ListType(ModelType(ReferenceKeyModel),
                              default=[{
                                  'resource_type': 'inventory.Server',
                                  'reference_key': 'reference.resource_id'
                              }, {
                                  'resource_type': 'inventory.CloudService',
                                  'reference_key': 'reference.resource_id'
                              }])


class PluginVerifyModel(Model):
    options = ModelType(PluginOptionsModel, default=PluginOptionsModel)


class PluginVerifyResponseModel(Model):
    resource_type = StringType(required=True, default='monitoring.DataSource')
    actions = ListType(DictType(StringType))
    result = ModelType(PluginVerifyModel, required=True, default=PluginVerifyModel)

