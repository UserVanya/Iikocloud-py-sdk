# TransportStopListsClearStopListRequest

Request to clear out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_clear_stop_list_request import TransportStopListsClearStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsClearStopListRequest from a JSON string
transport_stop_lists_clear_stop_list_request_instance = TransportStopListsClearStopListRequest.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsClearStopListRequest.to_json())

# convert the object into a dict
transport_stop_lists_clear_stop_list_request_dict = transport_stop_lists_clear_stop_list_request_instance.to_dict()
# create an instance of TransportStopListsClearStopListRequest from a dict
transport_stop_lists_clear_stop_list_request_from_dict = TransportStopListsClearStopListRequest.from_dict(transport_stop_lists_clear_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


