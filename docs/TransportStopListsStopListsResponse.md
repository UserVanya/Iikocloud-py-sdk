# TransportStopListsStopListsResponse

Status of out-of-stock lists for a specified organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**terminal_group_stop_lists** | [**List[TransportCommonRmsItemsResponseWrapperTerminalGroupStopList]**](TransportCommonRmsItemsResponseWrapperTerminalGroupStopList.md) | Set of out-of-stock lists | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_stop_lists_response import TransportStopListsStopListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsStopListsResponse from a JSON string
transport_stop_lists_stop_lists_response_instance = TransportStopListsStopListsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsStopListsResponse.to_json())

# convert the object into a dict
transport_stop_lists_stop_lists_response_dict = transport_stop_lists_stop_lists_response_instance.to_dict()
# create an instance of TransportStopListsStopListsResponse from a dict
transport_stop_lists_stop_lists_response_from_dict = TransportStopListsStopListsResponse.from_dict(transport_stop_lists_stop_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


