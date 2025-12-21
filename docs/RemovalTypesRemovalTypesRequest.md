# RemovalTypesRemovalTypesRequest

Request for organization's removal types (reasons for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations ids which removal types needs to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.removal_types_removal_types_request import RemovalTypesRemovalTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalTypesRemovalTypesRequest from a JSON string
removal_types_removal_types_request_instance = RemovalTypesRemovalTypesRequest.from_json(json)
# print the JSON string representation of the object
print(RemovalTypesRemovalTypesRequest.to_json())

# convert the object into a dict
removal_types_removal_types_request_dict = removal_types_removal_types_request_instance.to_dict()
# create an instance of RemovalTypesRemovalTypesRequest from a dict
removal_types_removal_types_request_from_dict = RemovalTypesRemovalTypesRequest.from_dict(removal_types_removal_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


