# TransportReservesResponseReserveOrder

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
**conception** | [**TransportDeliveriesResponseOrderConception**](TransportDeliveriesResponseOrderConception.md) | Concept. | [optional] 
**guests_info** | [**TransportDeliveriesResponseOrderGuestsInfo**](TransportDeliveriesResponseOrderGuestsInfo.md) | Information about order guests. | 
**items** | [**List[TransportDeliveriesResponseOrderOrderItem]**](TransportDeliveriesResponseOrderOrderItem.md) | Order items. | 
**combos** | [**List[TransportDeliveriesResponseOrderOrderCombo]**](TransportDeliveriesResponseOrderOrderCombo.md) | Combo. | [optional] 
**payments** | [**List[TransportDeliveriesResponseOrderPaymentItem]**](TransportDeliveriesResponseOrderPaymentItem.md) | Payments. | [optional] 
**tips** | [**List[TransportDeliveriesResponseOrderTipsPaymentItem]**](TransportDeliveriesResponseOrderTipsPaymentItem.md) | Tips. | [optional] 
**discounts** | [**List[TransportDeliveriesResponseOrderDiscountItem]**](TransportDeliveriesResponseOrderDiscountItem.md) | Discounts. | [optional] 
**order_type** | [**TransportDeliveriesResponseOrderOrderType**](TransportDeliveriesResponseOrderOrderType.md) | Order type. | 
**terminal_group_id** | **str** | ID of the terminal group where the order is located. | 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**loyalty_info** | [**TransportDeliveriesResponseOrderLoyaltyInfo**](TransportDeliveriesResponseOrderLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**external_data** | [**List[TransportDeliveriesResponseOrderExternalData]**](TransportDeliveriesResponseOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_response_reserve_order import TransportReservesResponseReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesResponseReserveOrder from a JSON string
transport_reserves_response_reserve_order_instance = TransportReservesResponseReserveOrder.from_json(json)
# print the JSON string representation of the object
print(TransportReservesResponseReserveOrder.to_json())

# convert the object into a dict
transport_reserves_response_reserve_order_dict = transport_reserves_response_reserve_order_instance.to_dict()
# create an instance of TransportReservesResponseReserveOrder from a dict
transport_reserves_response_reserve_order_from_dict = TransportReservesResponseReserveOrder.from_dict(transport_reserves_response_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


