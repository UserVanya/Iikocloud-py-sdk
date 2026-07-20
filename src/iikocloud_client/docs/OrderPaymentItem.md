# OrderPaymentItem

Payments details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 
**payment_type_id** | **UUID** | Payment type ID. | 
**sum** | **float** | Amount due | 

## Example

```python
from iikocloud_client.models.order_payment_item import OrderPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPaymentItem from a JSON string
order_payment_item_instance = OrderPaymentItem.from_json(json)
# print the JSON string representation of the object
print(OrderPaymentItem.to_json())

# convert the object into a dict
order_payment_item_dict = order_payment_item_instance.to_dict()
# create an instance of OrderPaymentItem from a dict
order_payment_item_from_dict = OrderPaymentItem.from_dict(order_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


