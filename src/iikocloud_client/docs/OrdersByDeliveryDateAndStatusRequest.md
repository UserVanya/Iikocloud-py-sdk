# OrdersByDeliveryDateAndStatusRequest

Request for information about orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_ids** | **List[UUID]** | List of driver IDs. | [optional] 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**source_keys** | **List[str]** | Source keys. | [optional] 
**statuses** | [**List[DeliveryStatus]**](DeliveryStatus.md) | Allowed order statuses. | [optional] 

## Example

```python
from iikocloud_client.models.orders_by_delivery_date_and_status_request import OrdersByDeliveryDateAndStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersByDeliveryDateAndStatusRequest from a JSON string
orders_by_delivery_date_and_status_request_instance = OrdersByDeliveryDateAndStatusRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersByDeliveryDateAndStatusRequest.to_json())

# convert the object into a dict
orders_by_delivery_date_and_status_request_dict = orders_by_delivery_date_and_status_request_instance.to_dict()
# create an instance of OrdersByDeliveryDateAndStatusRequest from a dict
orders_by_delivery_date_and_status_request_from_dict = OrdersByDeliveryDateAndStatusRequest.from_dict(orders_by_delivery_date_and_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


