# TransportDeliveriesRequestCreateOrderOrder

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. Must be unique.  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 
**external_number** | **str** | Order external number.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**complete_before** | **str** | Order fulfillment date.  &gt; Date and time must be local for delivery terminal, without time zone (take a look at example).   &gt; If null, order is urgent and time is calculated based on customer settings,  &gt; i.e. the shortest delivery time possible.  &gt; Permissible values: from current day and 60 days on. | [optional] 
**phone** | **str** | Telephone number.  &gt; Must begin with symbol \&quot;+\&quot; and must be at least 8 digits. | 
**order_type_id** | **str** | Order type ID.     Can be obtained by &#x60;/api/1/deliveries/order_types&#x60; operation.    &gt; Only one of the fields must be defined: **orderTypeId** or **orderServiceType**. | [optional] 
**order_service_type** | [**TransportDeliveriesRequestCreateOrderOrderServiceType**](TransportDeliveriesRequestCreateOrderOrderServiceType.md) | Order service type.  &gt; Only one of the fields must be defined: **orderTypeId** or **orderServiceType**.   &gt; Allowed from version &#x60;7.0.3&#x60;. | [optional] 
**delivery_point** | [**TransportDeliveriesRequestCreateOrderDeliveryPoint**](TransportDeliveriesRequestCreateOrderDeliveryPoint.md) | Delivery point details.  &gt; Not required in case of customer pickup. Otherwise, required. | [optional] 
**comment** | **str** | Order comment. | [optional] 
**customer** | [**TransportDeliveriesRequestCreateOrderCustomer**](TransportDeliveriesRequestCreateOrderCustomer.md) | Customer.                &#39;Regular&#39; customer:    - can be used only if a customer agrees to take part in the store&#39;s loyalty programs  - customer details will be added (updated) to the store&#39;s customer database  - benefits (accumulation of rewards, etc.) of active loyalty programs will be made available to the customer     &#39;One-time&#39; customer:    - should be used if a customer does not agree to take part in the store&#39;s loyalty programs or an aggregator (external system) does not provide customer details  - customer details will NOT be added to the store&#39;s customer database and will be used ONLY to complete the current order | [optional] 
**guests** | [**TransportDeliveriesRequestCreateOrderGuests**](TransportDeliveriesRequestCreateOrderGuests.md) | Guest details. Not equal to the customer who makes an order. | [optional] 
**marketing_source_id** | **str** | Marketing source (advertisement) ID.                 Can be obtained by &#x60;/api/1/marketing_sources&#x60; operation. | [optional] 
**operator_id** | **str** | Operator ID.   &gt; Allowed from version &#x60;7.6.3&#x60;. | [optional] 
**delivery_duration** | **int** | Delivery duration.   &gt; Allowed from version &#x60;8.8.6&#x60;. | [optional] 
**delivery_zone** | **str** | Name of delivery zone.   &gt; Allowed from version &#x60;8.8.6&#x60;. | [optional] 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items. | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos included in order. | [optional] 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payment components.   &gt; Type **LoyaltyCard** allowed from version &#x60;7.1.5&#x60;. | [optional] 
**tips** | [**List[TransportDeliveriesRequestCreateOrderTipsPayment]**](TransportDeliveriesRequestCreateOrderTipsPayment.md) | Order tips components. | [optional] 
**source_key** | **str** | The string key (marker) of the source (partner - api user) that created the order. Needed to limit the visibility of orders for external integration. | [optional] 
**discounts_info** | [**TransportDeliveriesRequestCreateOrderDiscountsInfo**](TransportDeliveriesRequestCreateOrderDiscountsInfo.md) | Discounts/surcharges. | [optional] 
**loyalty_info** | [**TransportDeliveriesRequestCreateOrderLoyaltyInfo**](TransportDeliveriesRequestCreateOrderLoyaltyInfo.md) | Information about Loyalty app. | [optional] 
**cheque_additional_info** | [**TransportDeliveriesCommonChequeAdditionalInfo**](TransportDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information. | [optional] 
**external_data** | [**List[TransportDeliveriesRequestCreateOrderExternalData]**](TransportDeliveriesRequestCreateOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_order import TransportDeliveriesRequestCreateOrderOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderOrder from a JSON string
transport_deliveries_request_create_order_order_instance = TransportDeliveriesRequestCreateOrderOrder.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderOrder.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_order_dict = transport_deliveries_request_create_order_order_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderOrder from a dict
transport_deliveries_request_create_order_order_from_dict = TransportDeliveriesRequestCreateOrderOrder.from_dict(transport_deliveries_request_create_order_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


