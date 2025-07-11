# TransportDeliveriesResponseOrderOrder

Order details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_delivery_id** | **str** | ID of delivery serving as source for splitting by FCRs. | [optional] 
**customer** | [**TransportDeliveriesResponseOrderCustomer**](TransportDeliveriesResponseOrderCustomer.md) | Delivery customer. | [optional] 
**phone** | **str** | Delivery phone number. | 
**delivery_point** | [**TransportDeliveriesResponseOrderDeliveryPoint**](TransportDeliveriesResponseOrderDeliveryPoint.md) | Delivery point details.  &lt;remarks&gt;  Not required if order type is customer pickup. Otherwise, required.  &lt;/remarks&gt; | [optional] 
**status** | [**TransportDeliveriesCommonDeliveryStatus**](TransportDeliveriesCommonDeliveryStatus.md) | Delivery status.                &gt; Delivery status &#x60;ReadyForCooking&#x60; is deprecated from version &#x60;9.0.6&#x60;. | 
**cancel_info** | [**TransportDeliveriesResponseOrderCancelInfo**](TransportDeliveriesResponseOrderCancelInfo.md) | Delivery cancellation details.  &lt;remarks&gt;  Required only if delivery is canceled, i.e. status&#x3D;Canceled.  &lt;/remarks&gt; | [optional] 
**courier_info** | [**TransportDeliveriesResponseOrderCourierInfo**](TransportDeliveriesResponseOrderCourierInfo.md) | Driver information. | [optional] 
**complete_before** | **str** | Order fulfillment time (Local for the terminal). | 
**when_created** | **str** | Delivery creation time in iikoFront (Local for the terminal). | 
**when_confirmed** | **str** | Delivery confirmation time (Local for the terminal). | [optional] 
**when_printed** | **str** | Service printing time (Local for the terminal). | [optional] 
**when_cooking_completed** | **str** | Cooking completion time (Local for the terminal). | [optional] 
**when_sended** | **str** | Delivery dispatch time (Local for the terminal). | [optional] 
**when_delivered** | **str** | Actual delivery time (Local for delivery terminal). | [optional] 
**comment** | **str** | Order comment. | [optional] 
**problem** | [**TransportDeliveriesResponseOrderProblem**](TransportDeliveriesResponseOrderProblem.md) | Problem flag. | [optional] 
**operator** | [**TransportDeliveriesResponseOrderEmployee**](TransportDeliveriesResponseOrderEmployee.md) | Operator that took order. | [optional] 
**marketing_source** | [**TransportDeliveriesResponseOrderMarketingSource**](TransportDeliveriesResponseOrderMarketingSource.md) | Marketing source. | [optional] 
**delivery_duration** | **int** | Duration of delivery (in minutes). | [optional] 
**index_in_courier_route** | **int** | Ordinal number in route list.  &lt;remarks&gt;  Field is filled up at the time of delivery allocation by logistics in iikoFront.  If logistics is not in use, the field is not filled up.  &lt;/remarks&gt; | [optional] 
**cooking_start_time** | **str** | The time when you need to start cooking an order (Local for the terminal). | 
**is_deleted** | **bool** | Order is deleted. | [optional] 
**when_received_by_api** | **str** | Moment of time when CloudAPI received the request to create the order (UTC). | [optional] 
**when_received_from_front** | **str** | Moment of time when the order first received and saved from iikoFront (UTC). | [optional] 
**moved_from_delivery_id** | **str** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_terminal_group_id** | **str** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_organization_id** | **str** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**external_courier_service** | [**TransportDeliveriesResponseOrderExternalCourierService**](TransportDeliveriesResponseOrderExternalCourierService.md) | ECS info.   &gt; Allowed from version &#x60;7.7.7&#x60;. | [optional] 
**moved_to_delivery_id** | **str** | Tells that this delivery has been canceled and moved to terminal group  with id *MovedToTerminalGroupId*. | [optional] 
**moved_to_terminal_group_id** | **str** |  | [optional] 
**moved_to_organization_id** | **str** |  | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**delivery_zone** | **str** | Name of delivery zone. | [optional] 
**estimated_time** | **str** | Delivery estimated time. | [optional] 
**is_asap** | **bool** | Whether to deliver as soon as possible. | [optional] 
**when_packed** | **str** | Delivery packing time (Local for the terminal). | [optional] 
**sum** | **float** | Order amount (after discount or surcharge). | 
**number** | **int** | Delivery No. | 
**source_key** | **str** | Delivery source. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 
**conception** | [**TransportDeliveriesResponseOrderConception**](TransportDeliveriesResponseOrderConception.md) | Concept. | [optional] 
**guests_info** | [**TransportDeliveriesResponseOrderGuestsInfo**](TransportDeliveriesResponseOrderGuestsInfo.md) | Information about order guests. | 
**items** | [**List[TransportDeliveriesResponseOrderOrderItem]**](TransportDeliveriesResponseOrderOrderItem.md) | Order items. | 
**combos** | [**List[TransportDeliveriesResponseOrderOrderCombo]**](TransportDeliveriesResponseOrderOrderCombo.md) | Combo. | [optional] 
**payments** | [**List[TransportDeliveriesResponseOrderPaymentItem]**](TransportDeliveriesResponseOrderPaymentItem.md) | Payments. | [optional] 
**tips** | [**List[TransportDeliveriesResponseOrderTipsPaymentItem]**](TransportDeliveriesResponseOrderTipsPaymentItem.md) | Tips. | [optional] 
**discounts** | [**List[TransportDeliveriesResponseOrderDiscountItem]**](TransportDeliveriesResponseOrderDiscountItem.md) | Discounts. | [optional] 
**order_type** | [**TransportDeliveriesResponseOrderOrderType**](TransportDeliveriesResponseOrderOrderType.md) | Order type. | 
**terminal_group_id** | **str** | ID of the terminal group where the order is located. | 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**loyalty_info** | [**TransportDeliveriesResponseOrderLoyaltyInfo**](TransportDeliveriesResponseOrderLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**external_data** | [**List[TransportDeliveriesResponseOrderExternalData]**](TransportDeliveriesResponseOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_order import TransportDeliveriesResponseOrderOrder

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderOrder from a JSON string
transport_deliveries_response_order_order_instance = TransportDeliveriesResponseOrderOrder.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderOrder.to_json())

# convert the object into a dict
transport_deliveries_response_order_order_dict = transport_deliveries_response_order_order_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderOrder from a dict
transport_deliveries_response_order_order_from_dict = TransportDeliveriesResponseOrderOrder.from_dict(transport_deliveries_response_order_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


