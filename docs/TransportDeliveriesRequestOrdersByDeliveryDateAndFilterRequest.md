# TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest

Request for information about orders from external source and based on additional filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_ids** | **List[str]** | List of terminal groups IDs. | [optional] 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**statuses** | [**List[TransportDeliveriesCommonDeliveryStatus]**](TransportDeliveriesCommonDeliveryStatus.md) | Allowed order statuses. | [optional] 
**has_problem** | **bool** | If true, delivery has a problem.  &gt; Conditions under which the order has a problem:  &gt; * order.problem.hasProblem is true;  &gt; * order status is Unconfirmed and CookingStartTime before now;  &gt; * order status is ReadyForCooking and (CookingStartTime + timeToCookingErrorTimeout) before now;  &gt; * order status is CookingCompleted or Waiting and (CookingStartTime + cookingTimeout) before now. | [optional] 
**order_service_type** | [**TransportDeliveriesRequestCreateOrderOrderServiceType**](TransportDeliveriesRequestCreateOrderOrderServiceType.md) | Order service type. | [optional] 
**search_text** | **str** | Value for search. Used for prefix search. | [optional] 
**time_to_cooking_error_timeout** | **int** | Error timeout for status time to cooking, in seconds. | [optional] 
**cooking_timeout** | **int** | Expected cooking time, in seconds. | [optional] 
**sort_property** | [**TransportDeliveriesRequestOrderSortProperty**](TransportDeliveriesRequestOrderSortProperty.md) | Sorting property. | [optional] 
**sort_direction** | [**TransportCommonSortDirection**](TransportCommonSortDirection.md) | Sorting direction. | [optional] 
**rows_count** | **int** | Maximum number of items returned. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**order_ids** | **List[str]** | Order IDs.                &gt; Must be null if \&quot;posOrderIds\&quot; is not null. | [optional] 
**pos_order_ids** | **List[str]** | POS order IDs.                &gt; Must be null if \&quot;orderIds\&quot; is not null. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_filter_request import TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest from a JSON string
transport_deliveries_request_orders_by_delivery_date_and_filter_request_instance = TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.to_json())

# convert the object into a dict
transport_deliveries_request_orders_by_delivery_date_and_filter_request_dict = transport_deliveries_request_orders_by_delivery_date_and_filter_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest from a dict
transport_deliveries_request_orders_by_delivery_date_and_filter_request_from_dict = TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest.from_dict(transport_deliveries_request_orders_by_delivery_date_and_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


