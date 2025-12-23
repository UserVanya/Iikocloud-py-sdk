# DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier

Change order's delivery type to DeliveryByCourier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_point** | [**DeliveriesRequestCreateOrderDeliveryPoint**](DeliveriesRequestCreateOrderDeliveryPoint.md) | Address of delivery. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_service_type_delivery_by_courier import DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier from a JSON string
deliveries_request_update_order_change_service_type_delivery_by_courier_instance = DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.to_json())

# convert the object into a dict
deliveries_request_update_order_change_service_type_delivery_by_courier_dict = deliveries_request_update_order_change_service_type_delivery_by_courier_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier from a dict
deliveries_request_update_order_change_service_type_delivery_by_courier_from_dict = DeliveriesRequestUpdateOrderChangeServiceTypeDeliveryByCourier.from_dict(deliveries_request_update_order_change_service_type_delivery_by_courier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


