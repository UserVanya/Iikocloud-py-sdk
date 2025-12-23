# StopListsCheckStopListRequest

Request for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.    Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items. | 

## Example

```python
from iikocloud_client.models.stop_lists_check_stop_list_request import StopListsCheckStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsCheckStopListRequest from a JSON string
stop_lists_check_stop_list_request_instance = StopListsCheckStopListRequest.from_json(json)
# print the JSON string representation of the object
print(StopListsCheckStopListRequest.to_json())

# convert the object into a dict
stop_lists_check_stop_list_request_dict = stop_lists_check_stop_list_request_instance.to_dict()
# create an instance of StopListsCheckStopListRequest from a dict
stop_lists_check_stop_list_request_from_dict = StopListsCheckStopListRequest.from_dict(stop_lists_check_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


