# TransportStopListsCheckStopListResponse

Response for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**rejected_items** | [**List[TransportStopListsStopListItem]**](TransportStopListsStopListItem.md) | Set of items in out-of-stock list.                If null, none of requested items are in out-of-stock list.  &gt; Present in response only if **not null**. | [optional] 

## Example

```python
from iikocloud_client.models.transport_stop_lists_check_stop_list_response import TransportStopListsCheckStopListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsCheckStopListResponse from a JSON string
transport_stop_lists_check_stop_list_response_instance = TransportStopListsCheckStopListResponse.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsCheckStopListResponse.to_json())

# convert the object into a dict
transport_stop_lists_check_stop_list_response_dict = transport_stop_lists_check_stop_list_response_instance.to_dict()
# create an instance of TransportStopListsCheckStopListResponse from a dict
transport_stop_lists_check_stop_list_response_from_dict = TransportStopListsCheckStopListResponse.from_dict(transport_stop_lists_check_stop_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


