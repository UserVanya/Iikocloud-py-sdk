# TableOrderResponsePayload

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combos** | [**List[OrderCombo]**](OrderCombo.md) | Combo. | [optional] 
**conception** | [**Conception**](Conception.md) | Concept. | [optional] 
**customer** | [**DeliveryOrderResponseRegularCustomer**](DeliveryOrderResponseRegularCustomer.md) | Guest.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**discounts** | [**List[DiscountItem]**](DiscountItem.md) | Discounts. | [optional] 
**external_data** | [**List[DeliveryOrderResponseExternalData]**](DeliveryOrderResponseExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**guests_info** | [**DeliveryOrderResponseGuestsInfo**](DeliveryOrderResponseGuestsInfo.md) | Information about order guests. | 
**items** | [**List[DeliveryOrderResponseItem]**](DeliveryOrderResponseItem.md) | Order items. | 
**loyalty_info** | [**DeliveryOrderResponseLoyaltyInfo**](DeliveryOrderResponseLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**number** | **int** | Delivery No. | 
**order_type** | [**DeliveryOrderResponseType**](DeliveryOrderResponseType.md) | Order type. | 
**payments** | [**List[PaymentItem]**](PaymentItem.md) | Payments. | [optional] 
**phone** | **str** | Guest phone.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**price_category** | [**CommonPriceCategory**](CommonPriceCategory.md) | Price Category of the order.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**source_key** | **str** | Delivery source. | [optional] 
**split_order_between_cash_registers** | [**SplitOrderBetweenCashRegisters**](SplitOrderBetweenCashRegisters.md) | Need to split order between cash registers.  &lt;remarks&gt;  Not empty for orders in statuses New or Bill.  &lt;/remarks&gt; | [optional] 
**status** | [**DeliveryOrderResponseStatus**](DeliveryOrderResponseStatus.md) | Order status. | 
**sum** | **float** | Order amount (after discount or surcharge). | 
**tab_name** | **str** | Tab name (only for fastfood terminals group in tab mode). | [optional] 
**table_ids** | **List[UUID]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**tips** | [**List[TipsPaymentItem]**](TipsPaymentItem.md) | Tips. | [optional] 
**waiter** | [**DeliveryOrderResponseEmployee**](DeliveryOrderResponseEmployee.md) | Order waiter. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 
**when_created** | **str** | Order creation date (terminal time zone). | [optional] 

## Example

```python
from iikocloud_client.models.table_order_response_payload import TableOrderResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderResponsePayload from a JSON string
table_order_response_payload_instance = TableOrderResponsePayload.from_json(json)
# print the JSON string representation of the object
print(TableOrderResponsePayload.to_json())

# convert the object into a dict
table_order_response_payload_dict = table_order_response_payload_instance.to_dict()
# create an instance of TableOrderResponsePayload from a dict
table_order_response_payload_from_dict = TableOrderResponsePayload.from_dict(table_order_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


