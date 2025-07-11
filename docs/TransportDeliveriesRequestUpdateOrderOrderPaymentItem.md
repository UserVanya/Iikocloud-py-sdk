# TransportDeliveriesRequestUpdateOrderOrderPaymentItem

Payments details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **float** | Amount due | 
**payment_type_id** | **str** | Payment type ID. | 
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_order_payment_item import TransportDeliveriesRequestUpdateOrderOrderPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderOrderPaymentItem from a JSON string
transport_deliveries_request_update_order_order_payment_item_instance = TransportDeliveriesRequestUpdateOrderOrderPaymentItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderOrderPaymentItem.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_order_payment_item_dict = transport_deliveries_request_update_order_order_payment_item_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderOrderPaymentItem from a dict
transport_deliveries_request_update_order_order_payment_item_from_dict = TransportDeliveriesRequestUpdateOrderOrderPaymentItem.from_dict(transport_deliveries_request_update_order_order_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


