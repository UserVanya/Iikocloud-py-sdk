# TableOrderErrorWebHookEventInfo

WebHook notification about table order saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**TableOrderInfo**](TableOrderInfo.md) | Event details. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**event_type** | **str** | Event type. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.table_order_error_web_hook_event_info import TableOrderErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderErrorWebHookEventInfo from a JSON string
table_order_error_web_hook_event_info_instance = TableOrderErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(TableOrderErrorWebHookEventInfo.to_json())

# convert the object into a dict
table_order_error_web_hook_event_info_dict = table_order_error_web_hook_event_info_instance.to_dict()
# create an instance of TableOrderErrorWebHookEventInfo from a dict
table_order_error_web_hook_event_info_from_dict = TableOrderErrorWebHookEventInfo.from_dict(table_order_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


