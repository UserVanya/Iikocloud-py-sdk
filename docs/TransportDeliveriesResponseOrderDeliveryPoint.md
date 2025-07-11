# TransportDeliveriesResponseOrderDeliveryPoint

Delivery address coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**TransportDeliveriesCommonCoordinates**](TransportDeliveriesCommonCoordinates.md) | Delivery address coordinates. | [optional] 
**address** | [**TransportDeliveriesResponseOrderAddress**](TransportDeliveriesResponseOrderAddress.md) | Delivery address details. | [optional] 
**external_cartography_id** | **str** | Address ID in external mapping system. | [optional] 
**comment** | **str** | Comment. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_delivery_point import TransportDeliveriesResponseOrderDeliveryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderDeliveryPoint from a JSON string
transport_deliveries_response_order_delivery_point_instance = TransportDeliveriesResponseOrderDeliveryPoint.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderDeliveryPoint.to_json())

# convert the object into a dict
transport_deliveries_response_order_delivery_point_dict = transport_deliveries_response_order_delivery_point_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderDeliveryPoint from a dict
transport_deliveries_response_order_delivery_point_from_dict = TransportDeliveriesResponseOrderDeliveryPoint.from_dict(transport_deliveries_response_order_delivery_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


