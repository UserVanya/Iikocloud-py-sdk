# IikoTransportPublicApiContractsDeliveriesResponseOrderOrder

Order details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_delivery_id** | **UUID** | ID of delivery serving as source for splitting by FCRs. | [optional] 
**customer** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCustomer**](IikoTransportPublicApiContractsDeliveriesResponseOrderCustomer.md) | Delivery customer. | [optional] 
**phone** | **str** | Delivery phone number. | 
**phone_extension** | **str** | Extension delivery phone number. | [optional] 
**delivery_point** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderDeliveryPoint**](IikoTransportPublicApiContractsDeliveriesResponseOrderDeliveryPoint.md) | Delivery point details.  &lt;remarks&gt;  Not required if order type is customer pickup. Otherwise, required.  &lt;/remarks&gt; | [optional] 
**status** | [**IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus**](IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus.md) | Delivery status.                &gt; Delivery status &#x60;ReadyForCooking&#x60; is deprecated from version &#x60;9.0.6&#x60;. | 
**cancel_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo.md) | Delivery cancellation details.  &lt;remarks&gt;  Required only if delivery is canceled, i.e. status&#x3D;Canceled.  &lt;/remarks&gt; | [optional] 
**courier_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo.md) | Driver information. | [optional] 
**complete_before** | **str** | Order fulfillment time (Local for the terminal). | 
**when_created** | **str** | Delivery creation time in iikoFront (Local for the terminal). | 
**when_confirmed** | **str** | Delivery confirmation time (Local for the terminal). | [optional] 
**when_printed** | **str** | Service printing time (Local for the terminal). | [optional] 
**when_cooking_completed** | **str** | Cooking completion time (Local for the terminal). | [optional] 
**when_sended** | **str** | Delivery dispatch time (Local for the terminal). | [optional] 
**when_delivered** | **str** | Actual delivery time (Local for delivery terminal). | [optional] 
**comment** | **str** | Order comment. | [optional] 
**problem** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderProblem**](IikoTransportPublicApiContractsDeliveriesResponseOrderProblem.md) | Problem flag. | [optional] 
**operator** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee**](IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee.md) | Operator that took order. | [optional] 
**marketing_source** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderMarketingSource**](IikoTransportPublicApiContractsDeliveriesResponseOrderMarketingSource.md) | Marketing source. | [optional] 
**delivery_duration** | **int** | Duration of delivery (in minutes). | [optional] 
**index_in_courier_route** | **int** | Ordinal number in route list.  &lt;remarks&gt;  Field is filled up at the time of delivery allocation by logistics in iikoFront.  If logistics is not in use, the field is not filled up.  &lt;/remarks&gt; | [optional] 
**cooking_start_time** | **str** | The time when you need to start cooking an order (Local for the terminal). | 
**is_deleted** | **bool** | Order is deleted. | [optional] 
**when_received_by_api** | **str** | Moment of time when CloudAPI received the request to create the order (UTC). | [optional] 
**when_received_from_front** | **str** | Moment of time when the order first received and saved from iikoFront (UTC). | [optional] 
**moved_from_delivery_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_terminal_group_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**moved_from_organization_id** | **UUID** | Tells that this delivery has been moved from terminal group  with id *MovedFromTerminalGroupId* by cancelling delivery with deliveryId *MovedFromDeliveryId*.   &gt; Allowed from version &#x60;7.5.4&#x60;. | [optional] 
**external_courier_service** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderExternalCourierService**](IikoTransportPublicApiContractsDeliveriesResponseOrderExternalCourierService.md) | ECS info.   &gt; Allowed from version &#x60;7.7.7&#x60;. | [optional] 
**moved_to_delivery_id** | **UUID** | Tells that this delivery has been canceled and moved to terminal group  with id *MovedToTerminalGroupId*. | [optional] 
**moved_to_terminal_group_id** | **UUID** |  | [optional] 
**moved_to_organization_id** | **UUID** |  | [optional] 
**menu_id** | **str** | External menu ID. | [optional] 
**delivery_zone** | **str** | Name of delivery zone. | [optional] 
**locked_at** | **str** | Timestamp of when the order was taken for editing (lock). | [optional] 
**estimated_time** | **str** | Delivery estimated time. | [optional] 
**is_asap** | **bool** | Whether to deliver as soon as possible. | [optional] 
**when_packed** | **str** | Delivery packing time (Local for the terminal). | [optional] 
**price_category** | [**IikoTransportPublicApiContractsCommonPriceCategory**](IikoTransportPublicApiContractsCommonPriceCategory.md) | Price category of the order.   &gt; Allowed from version &#x60;9.0.5&#x60;. | [optional] 
**tracking_link** | **str** | Order&#39;s tracking link. | [optional] 
**sum** | **float** | Order amount (after discount or surcharge). | 
**number** | **int** | Delivery No. | 
**source_key** | **str** | Delivery source. | [optional] 
**when_bill_printed** | **str** | Invoice printing time (guest bill time). | [optional] 
**when_closed** | **str** | Delivery closing time (Local for delivery terminal). | [optional] 
**conception** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderConception**](IikoTransportPublicApiContractsDeliveriesResponseOrderConception.md) | Concept. | [optional] 
**guests_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo.md) | Information about order guests. | 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem.md) | Order items. | 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderCombo.md) | Combo. | [optional] 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderPaymentItem.md) | Payments. | [optional] 
**tips** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderTipsPaymentItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderTipsPaymentItem.md) | Tips. | [optional] 
**discounts** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem]**](IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem.md) | Discounts. | [optional] 
**order_type** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderType.md) | Order type. | 
**terminal_group_id** | **UUID** | ID of the terminal group where the order is located. | 
**processed_payments_sum** | **float** | The amount of processed payments.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt;   &gt; Allowed from version &#x60;7.6.0&#x60;. | 
**loyalty_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderLoyaltyInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderLoyaltyInfo.md) | Information about Loyalty app.  &lt;remarks&gt;  null - only for unsupported POS versions.  &lt;/remarks&gt; | [optional] 
**external_data** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderExternalData]**](IikoTransportPublicApiContractsDeliveriesResponseOrderExternalData.md) | Order external data.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_order import IikoTransportPublicApiContractsDeliveriesResponseOrderOrder

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrder from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_order_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderOrder.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderOrder.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_dict = iiko_transport_public_api_contracts_deliveries_response_order_order_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrder from a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderOrder.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


