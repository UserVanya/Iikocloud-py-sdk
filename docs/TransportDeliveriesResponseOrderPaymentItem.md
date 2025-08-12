# TransportDeliveriesResponseOrderPaymentItem

Delivery order payment component.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | [**TransportDeliveriesResponseOrderPaymentType**](TransportDeliveriesResponseOrderPaymentType.md) | Payment type.                 Can be obtained by &#x60;/payment_types&#x60; operation. | 
**sum** | **float** | Amount due. | 
**is_preliminary** | **bool** | Whether payment item is preliminary. | 
**is_external** | **bool** | Payment item is external (created via biz.API). | 
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 
**is_fiscalized_externally** | **bool** | Whether the payment item is externally fiscalized.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**is_prepay** | **bool** | Whether the payment item is prepay.   &gt; Allowed from version &#x60;7.7.6&#x60;. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_payment_item import TransportDeliveriesResponseOrderPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderPaymentItem from a JSON string
transport_deliveries_response_order_payment_item_instance = TransportDeliveriesResponseOrderPaymentItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderPaymentItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_payment_item_dict = transport_deliveries_response_order_payment_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderPaymentItem from a dict
transport_deliveries_response_order_payment_item_from_dict = TransportDeliveriesResponseOrderPaymentItem.from_dict(transport_deliveries_response_order_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


