# ModifierSchemaListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ModifierSchema]**](ModifierSchema.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.modifier_schema_list_response import ModifierSchemaListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierSchemaListResponse from a JSON string
modifier_schema_list_response_instance = ModifierSchemaListResponse.from_json(json)
# print the JSON string representation of the object
print(ModifierSchemaListResponse.to_json())

# convert the object into a dict
modifier_schema_list_response_dict = modifier_schema_list_response_instance.to_dict()
# create an instance of ModifierSchemaListResponse from a dict
modifier_schema_list_response_from_dict = ModifierSchemaListResponse.from_dict(modifier_schema_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


