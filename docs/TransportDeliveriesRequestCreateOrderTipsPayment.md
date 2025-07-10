# TransportDeliveriesRequestCreateOrderTipsPayment

Base class of delivery order payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type_kind** | **str** |  | 
**tips_type_id** | **str** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | [optional] 
**sum** | **float** | Amount due. | 
**payment_type_id** | **str** | Payment type.                 Can be obtained by &#x60;/api/1/payment_types&#x60; operation. | 
**is_processed_externally** | **bool** | Whether payment item is processed by external payment system (made from outside). | [optional] 
**payment_additional_data** | [**TransportDeliveriesCommonPaymentAdditionalData**](TransportDeliveriesCommonPaymentAdditionalData.md) | Additional payment parameters. | [optional] 
**is_fiscalized_externally** | **bool** | Whether the payment item is externally fiscalized.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**is_prepay** | **bool** | Whether the payment item is prepay. Unavailable for &#x60;paymentKindType.LoyaltyCard&#x60;.   &gt; Allowed from version &#x60;8.2.6&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_tips_payment import TransportDeliveriesRequestCreateOrderTipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderTipsPayment from a JSON string
transport_deliveries_request_create_order_tips_payment_instance = TransportDeliveriesRequestCreateOrderTipsPayment.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderTipsPayment.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_tips_payment_dict = transport_deliveries_request_create_order_tips_payment_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderTipsPayment from a dict
transport_deliveries_request_create_order_tips_payment_from_dict = TransportDeliveriesRequestCreateOrderTipsPayment.from_dict(transport_deliveries_request_create_order_tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


