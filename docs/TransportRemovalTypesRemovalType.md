# TransportRemovalTypesRemovalType

Removal type (aka reason for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier. | 
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
from iikocloud_client.models.transport_removal_types_removal_type import TransportRemovalTypesRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportRemovalTypesRemovalType from a JSON string
transport_removal_types_removal_type_instance = TransportRemovalTypesRemovalType.from_json(json)
# print the JSON string representation of the object
print(TransportRemovalTypesRemovalType.to_json())

# convert the object into a dict
transport_removal_types_removal_type_dict = transport_removal_types_removal_type_instance.to_dict()
# create an instance of TransportRemovalTypesRemovalType from a dict
transport_removal_types_removal_type_from_dict = TransportRemovalTypesRemovalType.from_dict(transport_removal_types_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


