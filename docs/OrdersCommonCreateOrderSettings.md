# OrdersCommonCreateOrderSettings

Order creation options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for order to reach iikoFront.   After this time, order is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 
**check_stop_list** | **bool** | Flag indicating whether there&#39;s need to check order items in out-of-stock list.                Unable if &#x60;terminalGroupId&#x60; is null. | [optional] 

## Example

```python
from iikocloud_client.models.orders_common_create_order_settings import OrdersCommonCreateOrderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCommonCreateOrderSettings from a JSON string
orders_common_create_order_settings_instance = OrdersCommonCreateOrderSettings.from_json(json)
# print the JSON string representation of the object
print(OrdersCommonCreateOrderSettings.to_json())

# convert the object into a dict
orders_common_create_order_settings_dict = orders_common_create_order_settings_instance.to_dict()
# create an instance of OrdersCommonCreateOrderSettings from a dict
orders_common_create_order_settings_from_dict = OrdersCommonCreateOrderSettings.from_dict(orders_common_create_order_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


