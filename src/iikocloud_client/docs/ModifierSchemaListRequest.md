# ModifierSchemaListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[ModifierSchemaFilter]**](ModifierSchemaFilter.md) | Request filters. All filters are applied simultaneously (AND). See the method description for the list of supported filter fields | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 

## Example

```python
from iikocloud_client.models.modifier_schema_list_request import ModifierSchemaListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierSchemaListRequest from a JSON string
modifier_schema_list_request_instance = ModifierSchemaListRequest.from_json(json)
# print the JSON string representation of the object
print(ModifierSchemaListRequest.to_json())

# convert the object into a dict
modifier_schema_list_request_dict = modifier_schema_list_request_instance.to_dict()
# create an instance of ModifierSchemaListRequest from a dict
modifier_schema_list_request_from_dict = ModifierSchemaListRequest.from_dict(modifier_schema_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


