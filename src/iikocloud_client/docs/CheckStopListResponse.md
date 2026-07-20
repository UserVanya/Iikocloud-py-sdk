# CheckStopListResponse

Response for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**rejected_items** | [**List[StopListItem]**](StopListItem.md) | Set of items in out-of-stock list.                If null, none of requested items are in out-of-stock list.  &gt; Present in response only if **not null**. | [optional] 

## Example

```python
from iikocloud_client.models.check_stop_list_response import CheckStopListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckStopListResponse from a JSON string
check_stop_list_response_instance = CheckStopListResponse.from_json(json)
# print the JSON string representation of the object
print(CheckStopListResponse.to_json())

# convert the object into a dict
check_stop_list_response_dict = check_stop_list_response_instance.to_dict()
# create an instance of CheckStopListResponse from a dict
check_stop_list_response_from_dict = CheckStopListResponse.from_dict(check_stop_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


