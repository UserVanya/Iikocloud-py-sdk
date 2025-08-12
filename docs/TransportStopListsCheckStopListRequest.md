# TransportStopListsCheckStopListRequest

Request for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.    Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_check_stop_list_request import TransportStopListsCheckStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsCheckStopListRequest from a JSON string
transport_stop_lists_check_stop_list_request_instance = TransportStopListsCheckStopListRequest.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsCheckStopListRequest.to_json())

# convert the object into a dict
transport_stop_lists_check_stop_list_request_dict = transport_stop_lists_check_stop_list_request_instance.to_dict()
# create an instance of TransportStopListsCheckStopListRequest from a dict
transport_stop_lists_check_stop_list_request_from_dict = TransportStopListsCheckStopListRequest.from_dict(transport_stop_lists_check_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


