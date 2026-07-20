# ReserveOrderResponse

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combos** | [**List[OrderCombo]**](OrderCombo.md) | Combo. | [optional] 
**conception** | [**Conception**](Conception.md) | Concept. | [optional] 
**discounts** | [**List[DiscountItem]**](DiscountItem.md) | Discounts. | [optional] 
**external_data** | [**List[DeliveryOrderResponseExternalData]**](DeliveryOrderResponseExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**guests_info** | [**DeliveryOrderResponseGuestsInfo**](DeliveryOrderResponseGuestsInfo.md) | Information about order guests. | 
**items** | [**List[DeliveryOrderResponseItem]**](DeliveryOrderResponseItem.md) | Order items. | 
**loyalty_info** | [**DeliveryOrderResponseLoyaltyInfo**](DeliveryOrderResponseLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**number** | **int** | Delivery No. | 
**order_type** | [**DeliveryOrderResponseType**](DeliveryOrderResponseType.md) | Order type. | 
**payments** | [**List[PaymentItem]**](PaymentItem.md) | Payments. | [optional] 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**source_key** | **str** | Delivery source. | [optional] 
**sum** | **float** | Order amount (after discount or surcharge). | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**tips** | [**List[TipsPaymentItem]**](TipsPaymentItem.md) | Tips. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 

## Example

```python
from iikocloud_client.models.reserve_order_response import ReserveOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveOrderResponse from a JSON string
reserve_order_response_instance = ReserveOrderResponse.from_json(json)
# print the JSON string representation of the object
print(ReserveOrderResponse.to_json())

# convert the object into a dict
reserve_order_response_dict = reserve_order_response_instance.to_dict()
# create an instance of ReserveOrderResponse from a dict
reserve_order_response_from_dict = ReserveOrderResponse.from_dict(reserve_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


