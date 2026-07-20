# DeliveryOrderResponseDynamicDiscount

Dynamic discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **UUID** | Applied manual condition ID. | 
**sum** | **float** | Discount sum. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_dynamic_discount import DeliveryOrderResponseDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseDynamicDiscount from a JSON string
delivery_order_response_dynamic_discount_instance = DeliveryOrderResponseDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseDynamicDiscount.to_json())

# convert the object into a dict
delivery_order_response_dynamic_discount_dict = delivery_order_response_dynamic_discount_instance.to_dict()
# create an instance of DeliveryOrderResponseDynamicDiscount from a dict
delivery_order_response_dynamic_discount_from_dict = DeliveryOrderResponseDynamicDiscount.from_dict(delivery_order_response_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


