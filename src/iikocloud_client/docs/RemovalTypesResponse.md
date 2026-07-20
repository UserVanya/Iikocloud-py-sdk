# RemovalTypesResponse

Response with removal types (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**removal_types** | [**List[RemovalTypeDefinition]**](RemovalTypeDefinition.md) | List of removal types. | 

## Example

```python
from iikocloud_client.models.removal_types_response import RemovalTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalTypesResponse from a JSON string
removal_types_response_instance = RemovalTypesResponse.from_json(json)
# print the JSON string representation of the object
print(RemovalTypesResponse.to_json())

# convert the object into a dict
removal_types_response_dict = removal_types_response_instance.to_dict()
# create an instance of RemovalTypesResponse from a dict
removal_types_response_from_dict = RemovalTypesResponse.from_dict(removal_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


