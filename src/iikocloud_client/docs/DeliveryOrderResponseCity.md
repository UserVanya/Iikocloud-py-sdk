# DeliveryOrderResponseCity

City.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_city import DeliveryOrderResponseCity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseCity from a JSON string
delivery_order_response_city_instance = DeliveryOrderResponseCity.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseCity.to_json())

# convert the object into a dict
delivery_order_response_city_dict = delivery_order_response_city_instance.to_dict()
# create an instance of DeliveryOrderResponseCity from a dict
delivery_order_response_city_from_dict = DeliveryOrderResponseCity.from_dict(delivery_order_response_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


