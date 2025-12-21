# DeliveriesResponseOrderDiscountType

Discount type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_discount_type import DeliveriesResponseOrderDiscountType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderDiscountType from a JSON string
deliveries_response_order_discount_type_instance = DeliveriesResponseOrderDiscountType.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderDiscountType.to_json())

# convert the object into a dict
deliveries_response_order_discount_type_dict = deliveries_response_order_discount_type_instance.to_dict()
# create an instance of DeliveriesResponseOrderDiscountType from a dict
deliveries_response_order_discount_type_from_dict = DeliveriesResponseOrderDiscountType.from_dict(deliveries_response_order_discount_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


