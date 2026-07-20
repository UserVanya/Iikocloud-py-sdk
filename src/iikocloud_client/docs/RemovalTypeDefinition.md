# RemovalTypeDefinition

Removal type (aka reason for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_writeoff_to_cafe** | **bool** | Can write off to cafe. | [optional] 
**can_writeoff_to_user** | **bool** | Can write off to user. | [optional] 
**can_writeoff_to_waiter** | **bool** | Can write off to waiter. | [optional] 
**comment** | **str** | Comment. | [optional] 
**id** | **UUID** | Identifier. | 
**is_deleted** | **bool** | Is deleted sign. | [optional] 
**manual** | **bool** | Can be used manually. | [optional] 
**name** | **str** | Name of removal type. | 
**reason_required** | **bool** | Require comments on operations. | [optional] 

## Example

```python
from iikocloud_client.models.removal_type_definition import RemovalTypeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalTypeDefinition from a JSON string
removal_type_definition_instance = RemovalTypeDefinition.from_json(json)
# print the JSON string representation of the object
print(RemovalTypeDefinition.to_json())

# convert the object into a dict
removal_type_definition_dict = removal_type_definition_instance.to_dict()
# create an instance of RemovalTypeDefinition from a dict
removal_type_definition_from_dict = RemovalTypeDefinition.from_dict(removal_type_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


