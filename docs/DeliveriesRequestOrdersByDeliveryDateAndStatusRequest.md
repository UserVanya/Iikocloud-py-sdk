# DeliveriesRequestOrdersByDeliveryDateAndStatusRequest

Request for information about orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/api/1/deliveries/history/by_delivery_date_and_phone&#x60; method. | 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**statuses** | [**List[DeliveriesCommonDeliveryStatus]**](DeliveriesCommonDeliveryStatus.md) | Allowed order statuses. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**courier_ids** | **List[UUID]** | List of driver IDs. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_orders_by_delivery_date_and_status_request import DeliveriesRequestOrdersByDeliveryDateAndStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a JSON string
deliveries_request_orders_by_delivery_date_and_status_request_instance = DeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestOrdersByDeliveryDateAndStatusRequest.to_json())

# convert the object into a dict
deliveries_request_orders_by_delivery_date_and_status_request_dict = deliveries_request_orders_by_delivery_date_and_status_request_instance.to_dict()
# create an instance of DeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a dict
deliveries_request_orders_by_delivery_date_and_status_request_from_dict = DeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_dict(deliveries_request_orders_by_delivery_date_and_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


