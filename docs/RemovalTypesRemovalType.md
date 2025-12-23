# RemovalTypesRemovalType

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
from iikocloud_client.models.removal_types_removal_type import RemovalTypesRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalTypesRemovalType from a JSON string
removal_types_removal_type_instance = RemovalTypesRemovalType.from_json(json)
# print the JSON string representation of the object
print(RemovalTypesRemovalType.to_json())

# convert the object into a dict
removal_types_removal_type_dict = removal_types_removal_type_instance.to_dict()
# create an instance of RemovalTypesRemovalType from a dict
removal_types_removal_type_from_dict = RemovalTypesRemovalType.from_dict(removal_types_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


