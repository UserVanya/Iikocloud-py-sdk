# DeliveriesResponseOrderDeliveryPoint

Delivery address coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**DeliveriesCommonCoordinates**](DeliveriesCommonCoordinates.md) | Delivery address coordinates. | [optional] 
**address** | [**DeliveriesResponseOrderAddress**](DeliveriesResponseOrderAddress.md) | Delivery address details. | [optional] 
**external_cartography_id** | **str** | Address ID in external mapping system. | [optional] 
**comment** | **str** | Comment. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_delivery_point import DeliveriesResponseOrderDeliveryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderDeliveryPoint from a JSON string
deliveries_response_order_delivery_point_instance = DeliveriesResponseOrderDeliveryPoint.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderDeliveryPoint.to_json())

# convert the object into a dict
deliveries_response_order_delivery_point_dict = deliveries_response_order_delivery_point_instance.to_dict()
# create an instance of DeliveriesResponseOrderDeliveryPoint from a dict
deliveries_response_order_delivery_point_from_dict = DeliveriesResponseOrderDeliveryPoint.from_dict(deliveries_response_order_delivery_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


