# TransportTableOrdersRequestTableOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | [optional] 
**external_number** | **str** | Order external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**table_ids** | **List[str]** | Table IDs.                Can be obtained by &#x60;/api/1/reserve/available_restaurant_sections&#x60; operation. | [optional] 
**customer** | [**TransportDeliveriesRequestCreateOrderRegularCustomer**](TransportDeliveriesRequestCreateOrderRegularCustomer.md) | Guest.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**phone** | **str** | Guest phone.   &gt; Allowed from version &#x60;7.5.2&#x60;. | [optional] 
**guest_count** | **int** | Amount of guests in the order.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**guests** | [**TransportTableOrdersRequestGuestsInfo**](TransportTableOrdersRequestGuestsInfo.md) | Guests information.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**tab_name** | **str** | Tab name (only for fastfood terminals group in tab mode).   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items. | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos included in order. | [optional] 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**tips** | [**List[TransportDeliveriesRequestCreateOrderTipsPayment]**](TransportDeliveriesRequestCreateOrderTipsPayment.md) | Order tips components. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**discounts_info** | [**TransportDeliveriesRequestCreateOrderDiscountsInfo**](TransportDeliveriesRequestCreateOrderDiscountsInfo.md) | Discounts/surcharges. | [optional] 
**loyalty_info** | [**TransportDeliveriesRequestCreateOrderLoyaltyInfo**](TransportDeliveriesRequestCreateOrderLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**order_type_id** | **str** | Order type ID.                 Can be obtained by &#x60;/api/1/deliveries/order_types&#x60; operation | [optional] 
**cheque_additional_info** | [**TransportDeliveriesCommonChequeAdditionalInfo**](TransportDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**external_data** | [**List[TransportDeliveriesRequestCreateOrderExternalData]**](TransportDeliveriesRequestCreateOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_table_order import TransportTableOrdersRequestTableOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestTableOrder from a JSON string
transport_table_orders_request_table_order_instance = TransportTableOrdersRequestTableOrder.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestTableOrder.to_json())

# convert the object into a dict
transport_table_orders_request_table_order_dict = transport_table_orders_request_table_order_instance.to_dict()
# create an instance of TransportTableOrdersRequestTableOrder from a dict
transport_table_orders_request_table_order_from_dict = TransportTableOrdersRequestTableOrder.from_dict(transport_table_orders_request_table_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


