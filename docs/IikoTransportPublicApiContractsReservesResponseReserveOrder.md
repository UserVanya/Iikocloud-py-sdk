# IikoTransportPublicApiContractsReservesResponseReserveOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**menu_id** | **str** | External menu ID. | [optional] 
**sum** | **float** | Order amount (after discount or surcharge). | 
**number** | **int** | Delivery No. | 
**source_key** | **str** | Delivery source. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 
**conception** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderConception**](IikoTransportPublicApiContractsDeliveriesResponseOrderConception.md) | Concept. | [optional] 
**guests_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo.md) | Information about order guests. | 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem.md) | Order items. | 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo.md) | Combo. | [optional] 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentItem.md) | Payments. | [optional] 
**tips** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderTipsPaymentItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderTipsPaymentItem.md) | Tips. | [optional] 
**discounts** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem.md) | Discounts. | [optional] 
**order_type** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType.md) | Order type. | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**loyalty_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderLoyaltyInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**external_data** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderExternalData]**](IikoTransportPublicApiContractsDeliveriesResponseOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_response_reserve_order import IikoTransportPublicApiContractsReservesResponseReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesResponseReserveOrder from a JSON string
iiko_transport_public_api_contracts_reserves_response_reserve_order_instance = IikoTransportPublicApiContractsReservesResponseReserveOrder.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesResponseReserveOrder.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_response_reserve_order_dict = iiko_transport_public_api_contracts_reserves_response_reserve_order_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesResponseReserveOrder from a dict
iiko_transport_public_api_contracts_reserves_response_reserve_order_from_dict = IikoTransportPublicApiContractsReservesResponseReserveOrder.from_dict(iiko_transport_public_api_contracts_reserves_response_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


