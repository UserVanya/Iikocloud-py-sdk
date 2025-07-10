# TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier

Change order's delivery type to DeliveryByCourier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_point** | [**TransportDeliveriesRequestCreateOrderDeliveryPoint**](TransportDeliveriesRequestCreateOrderDeliveryPoint.md) | Address of delivery. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_service_type_delivery_by_courier import TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier from a JSON string
transport_deliveries_request_update_order_change_service_type_delivery_by_courier_instance = TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_service_type_delivery_by_courier_dict = transport_deliveries_request_update_order_change_service_type_delivery_by_courier_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier from a dict
transport_deliveries_request_update_order_change_service_type_delivery_by_courier_from_dict = TransportDeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.from_dict(transport_deliveries_request_update_order_change_service_type_delivery_by_courier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


