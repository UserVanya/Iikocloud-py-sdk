# DeliveriesRequestUpdateOrderOrderPaymentItem

Payments details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **float** | Amount due | 
**payment_type_id** | **UUID** | Payment type ID. | 
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_order_payment_item import DeliveriesRequestUpdateOrderOrderPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderOrderPaymentItem from a JSON string
deliveries_request_update_order_order_payment_item_instance = DeliveriesRequestUpdateOrderOrderPaymentItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderOrderPaymentItem.to_json())

# convert the object into a dict
deliveries_request_update_order_order_payment_item_dict = deliveries_request_update_order_order_payment_item_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderOrderPaymentItem from a dict
deliveries_request_update_order_order_payment_item_from_dict = DeliveriesRequestUpdateOrderOrderPaymentItem.from_dict(deliveries_request_update_order_order_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


