# TableOrdersResponseTableOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_ids** | **List[UUID]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | 
**customer** | [**DeliveriesResponseOrderRegularCustomer**](DeliveriesResponseOrderRegularCustomer.md) | Guest.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**phone** | **str** | Guest phone.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**status** | [**DeliveriesResponseOrderOrderStatus**](DeliveriesResponseOrderOrderStatus.md) | Order status. | 
**when_created** | **str** | Order creation date (terminal time zone). | [optional] 
**waiter** | [**DeliveriesResponseOrderEmployee**](DeliveriesResponseOrderEmployee.md) | Order waiter. | [optional] 
**tab_name** | **str** | Tab name (only for fastfood terminals group in tab mode). | [optional] 
**split_order_between_cash_registers** | [**TableOrdersResponseSplitOrderBetweenCashRegisters**](TableOrdersResponseSplitOrderBetweenCashRegisters.md) | Need to split order between cash registers.  &lt;remarks&gt;  Not empty for orders in statuses New or Bill.  &lt;/remarks&gt; | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**price_category** | [**CommonPriceCategory**](CommonPriceCategory.md) | Price Category of the order.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
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
from iikocloud_client.models.table_orders_response_table_order import TableOrdersResponseTableOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersResponseTableOrder from a JSON string
table_orders_response_table_order_instance = TableOrdersResponseTableOrder.from_json(json)
# print the JSON string representation of the object
print(TableOrdersResponseTableOrder.to_json())

# convert the object into a dict
table_orders_response_table_order_dict = table_orders_response_table_order_instance.to_dict()
# create an instance of TableOrdersResponseTableOrder from a dict
table_orders_response_table_order_from_dict = TableOrdersResponseTableOrder.from_dict(table_orders_response_table_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


