# ModifierSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.modifier_schema import ModifierSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierSchema from a JSON string
modifier_schema_instance = ModifierSchema.from_json(json)
# print the JSON string representation of the object
print(ModifierSchema.to_json())

# convert the object into a dict
modifier_schema_dict = modifier_schema_instance.to_dict()
# create an instance of ModifierSchema from a dict
modifier_schema_from_dict = ModifierSchema.from_dict(modifier_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


