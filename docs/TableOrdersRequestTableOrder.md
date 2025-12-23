# TableOrdersRequestTableOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | [optional] 
**external_number** | **str** | Order external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**table_ids** | **List[str]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | [optional] 
**customer** | [**DeliveriesRequestCreateOrderRegularCustomer**](DeliveriesRequestCreateOrderRegularCustomer.md) | Guest.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**phone** | **str** | Guest phone.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**guest_count** | **int** | Amount of guests in the order.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**guests** | [**TableOrdersRequestGuestsInfo**](TableOrdersRequestGuestsInfo.md) | Guests information.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**tab_name** | **str** | Tab name (only for fastfood terminals group in tab mode).   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**price_category_id** | **str** | Price category id of the order.    Can be obtained by &#x60;/api/2/menu&#x60; operation.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
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
from iikocloud_client.models.table_orders_request_table_order import TableOrdersRequestTableOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestTableOrder from a JSON string
table_orders_request_table_order_instance = TableOrdersRequestTableOrder.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestTableOrder.to_json())

# convert the object into a dict
table_orders_request_table_order_dict = table_orders_request_table_order_instance.to_dict()
# create an instance of TableOrdersRequestTableOrder from a dict
table_orders_request_table_order_from_dict = TableOrdersRequestTableOrder.from_dict(table_orders_request_table_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


