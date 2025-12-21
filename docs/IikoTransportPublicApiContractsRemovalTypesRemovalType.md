# IikoTransportPublicApiContractsRemovalTypesRemovalType

Removal type (aka reason for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier. | 
**name** | **str** | Name of removal type. | 
**comment** | **str** | Comment. | [optional] 
**can_writeoff_to_cafe** | **bool** | Can write off to cafe. | [optional] 
**can_writeoff_to_waiter** | **bool** | Can write off to waiter. | [optional] 
**can_writeoff_to_user** | **bool** | Can write off to user. | [optional] 
**reason_required** | **bool** | Require comments on operations. | [optional] 
**manual** | **bool** | Can be used manually. | [optional] 
**is_deleted** | **bool** | Is deleted sign. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_removal_types_removal_type import IikoTransportPublicApiContractsRemovalTypesRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalType from a JSON string
iiko_transport_public_api_contracts_removal_types_removal_type_instance = IikoTransportPublicApiContractsRemovalTypesRemovalType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsRemovalTypesRemovalType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_removal_types_removal_type_dict = iiko_transport_public_api_contracts_removal_types_removal_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalType from a dict
iiko_transport_public_api_contracts_removal_types_removal_type_from_dict = IikoTransportPublicApiContractsRemovalTypesRemovalType.from_dict(iiko_transport_public_api_contracts_removal_types_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


