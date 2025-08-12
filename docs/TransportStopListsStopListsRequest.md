# TransportStopListsStopListsRequest

DTO of out-of-stock lists request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations for which out-of-stock lists will be requested.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**return_size** | **bool** | Flag indicating the need to return the sizes of the dish. | [optional] 
**terminal_groups_ids** | **List[str]** | List of terminal groups for which you need to get out-of-stock lists.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.transport_stop_lists_stop_lists_request import TransportStopListsStopListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsStopListsRequest from a JSON string
transport_stop_lists_stop_lists_request_instance = TransportStopListsStopListsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsStopListsRequest.to_json())

# convert the object into a dict
transport_stop_lists_stop_lists_request_dict = transport_stop_lists_stop_lists_request_instance.to_dict()
# create an instance of TransportStopListsStopListsRequest from a dict
transport_stop_lists_stop_lists_request_from_dict = TransportStopListsStopListsRequest.from_dict(transport_stop_lists_stop_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


