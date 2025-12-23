# ReservesRequestReserveOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**menu_id** | **str** | External menu ID. | [optional] 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items. | 
**combos** | [**List[DeliveriesRequestCreateOrderCombo]**](DeliveriesRequestCreateOrderCombo.md) | Combos included in order. | [optional] 
**payments** | [**List[DeliveriesRequestCreateOrderPayment]**](DeliveriesRequestCreateOrderPayment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**tips** | [**List[DeliveriesRequestCreateOrderTipsPayment]**](DeliveriesRequestCreateOrderTipsPayment.md) | Order tips components. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**discounts_info** | [**DeliveriesRequestCreateOrderDiscountsInfo**](DeliveriesRequestCreateOrderDiscountsInfo.md) | Discounts/surcharges. | [optional] 
**loyalty_info** | [**DeliveriesRequestCreateOrderLoyaltyInfo**](DeliveriesRequestCreateOrderLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**order_type_id** | **str** | Order type ID.                 Can be obtained by &#x60;/api/1/deliveries/order_types&#x60; operation | [optional] 
**cheque_additional_info** | [**DeliveriesCommonChequeAdditionalInfo**](DeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**external_data** | [**List[DeliveriesRequestCreateOrderExternalData]**](DeliveriesRequestCreateOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_request_reserve_order import ReservesRequestReserveOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesRequestReserveOrder from a JSON string
reserves_request_reserve_order_instance = ReservesRequestReserveOrder.from_json(json)
# print the JSON string representation of the object
print(ReservesRequestReserveOrder.to_json())

# convert the object into a dict
reserves_request_reserve_order_dict = reserves_request_reserve_order_instance.to_dict()
# create an instance of ReservesRequestReserveOrder from a dict
reserves_request_reserve_order_from_dict = ReservesRequestReserveOrder.from_dict(reserves_request_reserve_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


