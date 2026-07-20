# DeliveryOrderResponsePayload

Order details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_info** | [**CancelInfo**](CancelInfo.md) | Delivery cancellation details.  &lt;remarks&gt;  Required only if delivery is canceled, i.e. status&#x3D;Canceled.  &lt;/remarks&gt; | [optional] 
**combos** | [**List[OrderCombo]**](OrderCombo.md) | Combo. | [optional] 
**comment** | **str** | Order comment. | [optional] 
**complete_before** | **str** | Order fulfillment time (Local for the terminal). | 
**conception** | [**Conception**](Conception.md) | Concept. | [optional] 
**cooking_start_time** | **str** | The time when you need to start cooking an order (Local for the terminal). | 
**courier_info** | [**CourierInfo**](CourierInfo.md) | Driver information. | [optional] 
**customer** | [**DeliveryOrderResponseCustomer**](DeliveryOrderResponseCustomer.md) | Delivery customer. | [optional] 
**delivery_duration** | **int** | Duration of delivery (in minutes). | [optional] 
**delivery_point** | [**DeliveryOrderResponsePoint**](DeliveryOrderResponsePoint.md) | Delivery point details.  &lt;remarks&gt;  Not required if order type is customer pickup. Otherwise, required.  &lt;/remarks&gt; | [optional] 
**delivery_zone** | **str** | Name of delivery zone. | [optional] 
**discounts** | [**List[DiscountItem]**](DiscountItem.md) | Discounts. | [optional] 
**estimated_time** | **str** | Delivery estimated time. | [optional] 
**external_courier_service** | [**ExternalCourierService**](ExternalCourierService.md) | ECS info.   &gt; Allowed from version &#x60;7.7.7&#x60;. | [optional] 
**external_data** | [**List[DeliveryOrderResponseExternalData]**](DeliveryOrderResponseExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**guests_info** | [**DeliveryOrderResponseGuestsInfo**](DeliveryOrderResponseGuestsInfo.md) | Information about order guests. | 
**index_in_courier_route** | **int** | Ordinal number in route list.  &lt;remarks&gt;  Field is filled up at the time of delivery allocation by logistics in iikoFront.  If logistics is not in use, the field is not filled up.  &lt;/remarks&gt; | [optional] 
**is_asap** | **bool** | Whether to deliver as soon as possible. | [optional] 
**is_deleted** | **bool** | Order is deleted. | [optional] 
**items** | [**List[DeliveryOrderResponseItem]**](DeliveryOrderResponseItem.md) | Order items. | 
**locked_at** | **str** | Timestamp of when the order was taken for editing (lock). | [optional] 
**loyalty_info** | [**DeliveryOrderResponseLoyaltyInfo**](DeliveryOrderResponseLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**marketing_source** | [**DeliveryOrderResponseMarketingSource**](DeliveryOrderResponseMarketingSource.md) | Marketing source. | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**moved_from_delivery_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_organization_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_terminal_group_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_to_delivery_id** | **UUID** | Tells that this delivery has been canceled and moved to terminal group  with id *MovedToTerminalGroupId*. | [optional] 
**moved_to_organization_id** | **UUID** |  | [optional] 
**moved_to_terminal_group_id** | **UUID** |  | [optional] 
**number** | **int** | Delivery No. | 
**operator** | [**DeliveryOrderResponseEmployee**](DeliveryOrderResponseEmployee.md) | Operator that took order. | [optional] 
**order_type** | [**DeliveryOrderResponseType**](DeliveryOrderResponseType.md) | Order type. | 
**parent_delivery_id** | **UUID** | ID of delivery serving as source for splitting by FCRs. | [optional] 
**payments** | [**List[PaymentItem]**](PaymentItem.md) | Payments. | [optional] 
**phone** | **str** | Delivery phone number. | 
**phone_extension** | **str** | Extension delivery phone number. | [optional] 
**price_category** | [**CommonPriceCategory**](CommonPriceCategory.md) | Price category of the order.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
**problem** | [**Problem**](Problem.md) | Problem flag. | [optional] 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**source_key** | **str** | Delivery source. | [optional] 
**status** | [**DeliveryStatus**](DeliveryStatus.md) | Delivery status.                &gt; Delivery status &#x60;ReadyForCooking&#x60; is deprecated from version &#x60;9.0.6&#x60;. | 
**sum** | **float** | Order amount (after discount or surcharge). | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**tips** | [**List[TipsPaymentItem]**](TipsPaymentItem.md) | Tips. | [optional] 
**tracking_link** | **str** | Order&#39;s tracking link. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 
**when_confirmed** | **str** | Delivery confirmation time (Local for the terminal). | [optional] 
**when_cooking_completed** | **str** | Cooking completion time (Local for the terminal). | [optional] 
**when_created** | **str** | Delivery creation time in iikoFront (Local for the terminal). | 
**when_delivered** | **str** | Actual delivery time (Local for delivery terminal). | [optional] 
**when_packed** | **str** | Delivery packing time (Local for the terminal). | [optional] 
**when_printed** | **str** | Service printing time (Local for the terminal). | [optional] 
**when_received_by_api** | **str** | Moment of time when CloudAPI received the request to create the order (UTC). | [optional] 
**when_received_from_front** | **str** | Moment of time when the order first received and saved from iikoFront (UTC). | [optional] 
**when_sended** | **str** | Delivery dispatch time (Local for the terminal). | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_payload import DeliveryOrderResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponsePayload from a JSON string
delivery_order_response_payload_instance = DeliveryOrderResponsePayload.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponsePayload.to_json())

# convert the object into a dict
delivery_order_response_payload_dict = delivery_order_response_payload_instance.to_dict()
# create an instance of DeliveryOrderResponsePayload from a dict
delivery_order_response_payload_from_dict = DeliveryOrderResponsePayload.from_dict(delivery_order_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


