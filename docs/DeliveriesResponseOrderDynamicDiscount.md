# DeliveriesResponseOrderDynamicDiscount

Dynamic discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **str** | Applied manual condition ID. | 
**sum** | **float** | Discount sum. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_dynamic_discount import DeliveriesResponseOrderDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderDynamicDiscount from a JSON string
deliveries_response_order_dynamic_discount_instance = DeliveriesResponseOrderDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderDynamicDiscount.to_json())

# convert the object into a dict
deliveries_response_order_dynamic_discount_dict = deliveries_response_order_dynamic_discount_instance.to_dict()
# create an instance of DeliveriesResponseOrderDynamicDiscount from a dict
deliveries_response_order_dynamic_discount_from_dict = DeliveriesResponseOrderDynamicDiscount.from_dict(deliveries_response_order_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


