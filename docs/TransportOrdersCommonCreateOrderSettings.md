# TransportOrdersCommonCreateOrderSettings

Order creation options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for order to reach iikoFront.   After this time, order is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 
**check_stop_list** | **bool** | Flag indicating whether there&#39;s need to check order items in out-of-stock list.                Unable if &#x60;terminalGroupId&#x60; is null. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_orders_common_create_order_settings import TransportOrdersCommonCreateOrderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrdersCommonCreateOrderSettings from a JSON string
transport_orders_common_create_order_settings_instance = TransportOrdersCommonCreateOrderSettings.from_json(json)
# print the JSON string representation of the object
print(TransportOrdersCommonCreateOrderSettings.to_json())

# convert the object into a dict
transport_orders_common_create_order_settings_dict = transport_orders_common_create_order_settings_instance.to_dict()
# create an instance of TransportOrdersCommonCreateOrderSettings from a dict
transport_orders_common_create_order_settings_from_dict = TransportOrdersCommonCreateOrderSettings.from_dict(transport_orders_common_create_order_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


