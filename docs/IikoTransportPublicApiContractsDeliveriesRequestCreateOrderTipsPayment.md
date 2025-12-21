# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment

Base class of delivery order payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type_kind** | **str** |  | 
**tips_type_id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/tips_types&#x60; operation. | [optional] 
**sum** | **float** | Amount due. | 
**payment_type_id** | **UUID** | Payment type.                 Can be obtained by &#x60;/payment_types&#x60; operation. | 
**is_processed_externally** | **bool** | Whether payment item is processed by external payment system (made from outside). | [optional] 
**payment_additional_data** | [**IikoTransportPublicApiContractsDeliveriesCommonPaymentAdditionalData**](IikoTransportPublicApiContractsDeliveriesCommonPaymentAdditionalData.md) | Additional payment parameters. | [optional] 
**is_fiscalized_externally** | **bool** | Whether the payment item is externally fiscalized.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**is_prepay** | **bool** | Whether the payment item is prepay. Unavailable for &#x60;paymentKindType.LoyaltyCard&#x60;.   &gt; Allowed from version &#x60;8.2.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_tips_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


