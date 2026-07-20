# OrdersByDeliveryDateAndFilterRequest

Request for information about orders from external source and based on additional filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooking_timeout** | **int** | Expected cooking time, in seconds. | [optional] 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | [optional] 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**has_problem** | **bool** | If true, delivery has a problem.  &gt; Conditions under which the order has a problem:  &gt; * order.problem.hasProblem is true;  &gt; * order status is Unconfirmed and CookingStartTime before now;  &gt; * order status is ReadyForCooking and (CookingStartTime + timeToCookingErrorTimeout) before now;  &gt; * order status is CookingCompleted or Waiting and (CookingStartTime + cookingTimeout) before now. | [optional] 
**order_ids** | **List[UUID]** | Order IDs.                &gt; Must be null if \&quot;posOrderIds\&quot; is not null. | [optional] 
**order_service_type** | [**DeliveryOrderCreateServiceType**](DeliveryOrderCreateServiceType.md) | Order service type. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**pos_order_ids** | **List[UUID]** | POS order IDs.                &gt; Must be null if \&quot;orderIds\&quot; is not null. | [optional] 
**rows_count** | **int** | Maximum number of items returned. | [optional] 
**search_text** | **str** | Value for search. Used for prefix search. | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) | Sorting direction. | [optional] 
**sort_property** | [**OrderSortProperty**](OrderSortProperty.md) | Sorting property. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**statuses** | [**List[DeliveryStatus]**](DeliveryStatus.md) | Allowed order statuses. | [optional] 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs. | [optional] 
**time_to_cooking_error_timeout** | **int** | Error timeout for status time to cooking, in seconds. | [optional] 

## Example

```python
from iikocloud_client.models.orders_by_delivery_date_and_filter_request import OrdersByDeliveryDateAndFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersByDeliveryDateAndFilterRequest from a JSON string
orders_by_delivery_date_and_filter_request_instance = OrdersByDeliveryDateAndFilterRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersByDeliveryDateAndFilterRequest.to_json())

# convert the object into a dict
orders_by_delivery_date_and_filter_request_dict = orders_by_delivery_date_and_filter_request_instance.to_dict()
# create an instance of OrdersByDeliveryDateAndFilterRequest from a dict
orders_by_delivery_date_and_filter_request_from_dict = OrdersByDeliveryDateAndFilterRequest.from_dict(orders_by_delivery_date_and_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


