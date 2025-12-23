# RemovalTypesRemovalTypesResponse

Response with removal types (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**removal_types** | [**List[RemovalTypesRemovalType]**](RemovalTypesRemovalType.md) | List of removal types. | 

## Example

```python
from iikocloud_client.models.removal_types_removal_types_response import RemovalTypesRemovalTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalTypesRemovalTypesResponse from a JSON string
removal_types_removal_types_response_instance = RemovalTypesRemovalTypesResponse.from_json(json)
# print the JSON string representation of the object
print(RemovalTypesRemovalTypesResponse.to_json())

# convert the object into a dict
removal_types_removal_types_response_dict = removal_types_removal_types_response_instance.to_dict()
# create an instance of RemovalTypesRemovalTypesResponse from a dict
removal_types_removal_types_response_from_dict = RemovalTypesRemovalTypesResponse.from_dict(removal_types_removal_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


