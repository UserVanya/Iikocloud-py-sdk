# ReserveOrderRequest

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**ChequeAdditionalInfo**](ChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**combos** | [**List[Combo]**](Combo.md) | Combos included in order. | [optional] 
**discounts_info** | [**DiscountsInfo**](DiscountsInfo.md) | Discounts/surcharges. | [optional] 
**external_data** | [**List[DeliveryOrderCreateExternalData]**](DeliveryOrderCreateExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items. | 
**loyalty_info** | [**DeliveryOrderCreateLoyaltyInfo**](DeliveryOrderCreateLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**order_type_id** | **UUID** | Order type ID.                 Can be obtained by &#x60;/api/1/deliveries/order_types&#x60; operation | [optional] 
**payments** | [**List[Payment]**](Payment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**tips** | [**List[TipsPayment]**](TipsPayment.md) | Order tips components. | [optional] 

## Example

```python
from iikocloud_client.models.reserve_order_request import ReserveOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveOrderRequest from a JSON string
reserve_order_request_instance = ReserveOrderRequest.from_json(json)
# print the JSON string representation of the object
print(ReserveOrderRequest.to_json())

# convert the object into a dict
reserve_order_request_dict = reserve_order_request_instance.to_dict()
# create an instance of ReserveOrderRequest from a dict
reserve_order_request_from_dict = ReserveOrderRequest.from_dict(reserve_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


