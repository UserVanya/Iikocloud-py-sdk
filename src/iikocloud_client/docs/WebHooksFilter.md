# WebHooksFilter

Webhooks filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_hours_and_mapping_update_filter** | [**WebHookShortFilter**](WebHookShortFilter.md) | Filter for business hours and mapping changes. | [optional] 
**delivery_order_filter** | [**DeliveryOrderWebHooksFilter**](DeliveryOrderWebHooksFilter.md) | Filter for delivery orders. | [optional] 
**nomenclature_update_filter** | [**WebHookShortFilter**](WebHookShortFilter.md) | Filter for nomenclature changes. | [optional] 
**personal_shift_filter** | [**WebHookShortFilter**](WebHookShortFilter.md) | Filter for personal shift. | [optional] 
**reserve_filter** | [**ReserveWebHookFilter**](ReserveWebHookFilter.md) | Filter for banquets/reserves. | [optional] 
**stop_list_update_filter** | [**WebHookShortFilter**](WebHookShortFilter.md) | Filter for stop-lists changes. | [optional] 
**table_order_filter** | [**TableOrderWebHookFilter**](TableOrderWebHookFilter.md) | Filter for table orders. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_filter import WebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksFilter from a JSON string
web_hooks_filter_instance = WebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(WebHooksFilter.to_json())

# convert the object into a dict
web_hooks_filter_dict = web_hooks_filter_instance.to_dict()
# create an instance of WebHooksFilter from a dict
web_hooks_filter_from_dict = WebHooksFilter.from_dict(web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


