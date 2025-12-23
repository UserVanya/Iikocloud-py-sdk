# StopListsCheckStopListResponse

Response for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**rejected_items** | [**List[StopListsStopListItem]**](StopListsStopListItem.md) | Set of items in out-of-stock list.                If null, none of requested items are in out-of-stock list.  &gt; Present in response only if **not null**. | [optional] 

## Example

```python
from iikocloud_client.models.stop_lists_check_stop_list_response import StopListsCheckStopListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsCheckStopListResponse from a JSON string
stop_lists_check_stop_list_response_instance = StopListsCheckStopListResponse.from_json(json)
# print the JSON string representation of the object
print(StopListsCheckStopListResponse.to_json())

# convert the object into a dict
stop_lists_check_stop_list_response_dict = stop_lists_check_stop_list_response_instance.to_dict()
# create an instance of StopListsCheckStopListResponse from a dict
stop_lists_check_stop_list_response_from_dict = StopListsCheckStopListResponse.from_dict(stop_lists_check_stop_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


