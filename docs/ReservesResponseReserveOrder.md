# ReservesResponseReserveOrder

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
**conception** | [**DeliveriesResponseOrderConception**](DeliveriesResponseOrderConception.md) | Concept. | [optional] 
**guests_info** | [**DeliveriesResponseOrderGuestsInfo**](DeliveriesResponseOrderGuestsInfo.md) | Information about order guests. | 
**items** | [**List[DeliveriesResponseOrderOrderItem]**](DeliveriesResponseOrderOrderItem.md) | Order items. | 
**combos** | [**List[DeliveriesResponseOrderOrderCombo]**](DeliveriesResponseOrderOrderCombo.md) | Combo. | [optional] 
**payments** | [**List[DeliveriesResponseOrderPaymentItem]**](DeliveriesResponseOrderPaymentItem.md) | Payments. | [optional] 
**tips** | [**List[DeliveriesResponseOrderTipsPaymentItem]**](DeliveriesResponseOrderTipsPaymentItem.md) | Tips. | [optional] 
**discounts** | [**List[DeliveriesResponseOrderDiscountItem]**](DeliveriesResponseOrderDiscountItem.md) | Discounts. | [optional] 
**order_type** | [**DeliveriesResponseOrderOrderType**](DeliveriesResponseOrderOrderType.md) | Order type. | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**loyalty_info** | [**DeliveriesResponseOrderLoyaltyInfo**](DeliveriesResponseOrderLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**external_data** | [**List[DeliveriesResponseOrderExternalData]**](DeliveriesResponseOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_response_reserve_order import ReservesResponseReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesResponseReserveOrder from a JSON string
reserves_response_reserve_order_instance = ReservesResponseReserveOrder.from_json(json)
# print the JSON string representation of the object
print(ReservesResponseReserveOrder.to_json())

# convert the object into a dict
reserves_response_reserve_order_dict = reserves_response_reserve_order_instance.to_dict()
# create an instance of ReservesResponseReserveOrder from a dict
reserves_response_reserve_order_from_dict = ReservesResponseReserveOrder.from_dict(reserves_response_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


