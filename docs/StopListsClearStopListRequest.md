# StopListsClearStopListRequest

Request to clear out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.stop_lists_clear_stop_list_request import StopListsClearStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsClearStopListRequest from a JSON string
stop_lists_clear_stop_list_request_instance = StopListsClearStopListRequest.from_json(json)
# print the JSON string representation of the object
print(StopListsClearStopListRequest.to_json())

# convert the object into a dict
stop_lists_clear_stop_list_request_dict = stop_lists_clear_stop_list_request_instance.to_dict()
# create an instance of StopListsClearStopListRequest from a dict
stop_lists_clear_stop_list_request_from_dict = StopListsClearStopListRequest.from_dict(stop_lists_clear_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


