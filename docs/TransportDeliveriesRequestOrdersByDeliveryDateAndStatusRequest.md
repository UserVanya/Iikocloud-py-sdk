# TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest

Request for information about orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/deliveries/history/by_delivery_date_and_phone&#x60; method. | 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**statuses** | [**List[TransportDeliveriesCommonDeliveryStatus]**](TransportDeliveriesCommonDeliveryStatus.md) | Allowed order statuses. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**courier_ids** | **List[str]** | List of driver IDs. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_orders_by_delivery_date_and_status_request import TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a JSON string
transport_deliveries_request_orders_by_delivery_date_and_status_request_instance = TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.to_json())

# convert the object into a dict
transport_deliveries_request_orders_by_delivery_date_and_status_request_dict = transport_deliveries_request_orders_by_delivery_date_and_status_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a dict
transport_deliveries_request_orders_by_delivery_date_and_status_request_from_dict = TransportDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_dict(transport_deliveries_request_orders_by_delivery_date_and_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


