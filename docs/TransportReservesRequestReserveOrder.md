# TransportReservesRequestReserveOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**menu_id** | **str** | External menu ID. | [optional] 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items. | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos included in order. | [optional] 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**tips** | [**List[TransportDeliveriesRequestCreateOrderTipsPayment]**](TransportDeliveriesRequestCreateOrderTipsPayment.md) | Order tips components. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**discounts_info** | [**TransportDeliveriesRequestCreateOrderDiscountsInfo**](TransportDeliveriesRequestCreateOrderDiscountsInfo.md) | Discounts/surcharges. | [optional] 
**loyalty_info** | [**TransportDeliveriesRequestCreateOrderLoyaltyInfo**](TransportDeliveriesRequestCreateOrderLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**order_type_id** | **str** | Order type ID.                 Can be obtained by &#x60;/deliveries/order_types&#x60; operation | [optional] 
**cheque_additional_info** | [**TransportDeliveriesCommonChequeAdditionalInfo**](TransportDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**external_data** | [**List[TransportDeliveriesRequestCreateOrderExternalData]**](TransportDeliveriesRequestCreateOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_reserves_request_reserve_order import TransportReservesRequestReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesRequestReserveOrder from a JSON string
transport_reserves_request_reserve_order_instance = TransportReservesRequestReserveOrder.from_json(json)
# print the JSON string representation of the object
print(TransportReservesRequestReserveOrder.to_json())

# convert the object into a dict
transport_reserves_request_reserve_order_dict = transport_reserves_request_reserve_order_instance.to_dict()
# create an instance of TransportReservesRequestReserveOrder from a dict
transport_reserves_request_reserve_order_from_dict = TransportReservesRequestReserveOrder.from_dict(transport_reserves_request_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


