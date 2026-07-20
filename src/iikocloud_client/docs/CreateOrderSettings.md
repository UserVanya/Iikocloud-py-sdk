# CreateOrderSettings

Order creation options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_stop_list** | **bool** | Flag indicating whether there&#39;s need to check order items in out-of-stock list.                Unable if &#x60;terminalGroupId&#x60; is null. | [optional] 
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for order to reach iikoFront.   After this time, order is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 

## Example

```python
from iikocloud_client.models.create_order_settings import CreateOrderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderSettings from a JSON string
create_order_settings_instance = CreateOrderSettings.from_json(json)
# print the JSON string representation of the object
print(CreateOrderSettings.to_json())

# convert the object into a dict
create_order_settings_dict = create_order_settings_instance.to_dict()
# create an instance of CreateOrderSettings from a dict
create_order_settings_from_dict = CreateOrderSettings.from_dict(create_order_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


