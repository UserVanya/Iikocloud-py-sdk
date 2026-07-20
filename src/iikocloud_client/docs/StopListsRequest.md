# StopListsRequest

DTO of out-of-stock lists request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations for which out-of-stock lists will be requested.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**return_size** | **bool** | Flag indicating the need to return the sizes of the dish. | [optional] 
**terminal_groups_ids** | **List[UUID]** | List of terminal groups for which you need to get out-of-stock lists.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.stop_lists_request import StopListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsRequest from a JSON string
stop_lists_request_instance = StopListsRequest.from_json(json)
# print the JSON string representation of the object
print(StopListsRequest.to_json())

# convert the object into a dict
stop_lists_request_dict = stop_lists_request_instance.to_dict()
# create an instance of StopListsRequest from a dict
stop_lists_request_from_dict = StopListsRequest.from_dict(stop_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


