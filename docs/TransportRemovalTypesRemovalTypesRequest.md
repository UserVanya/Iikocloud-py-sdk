# TransportRemovalTypesRemovalTypesRequest

Request for organization's removal types (reasons for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations ids which removal types needs to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_removal_types_removal_types_request import TransportRemovalTypesRemovalTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportRemovalTypesRemovalTypesRequest from a JSON string
transport_removal_types_removal_types_request_instance = TransportRemovalTypesRemovalTypesRequest.from_json(json)
# print the JSON string representation of the object
print(TransportRemovalTypesRemovalTypesRequest.to_json())

# convert the object into a dict
transport_removal_types_removal_types_request_dict = transport_removal_types_removal_types_request_instance.to_dict()
# create an instance of TransportRemovalTypesRemovalTypesRequest from a dict
transport_removal_types_removal_types_request_from_dict = TransportRemovalTypesRemovalTypesRequest.from_dict(transport_removal_types_removal_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


