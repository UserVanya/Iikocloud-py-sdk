# DeliveryOrderResponsePoint

Delivery address coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**DeliveryOrderResponseAddress**](DeliveryOrderResponseAddress.md) | Delivery address details. | [optional] 
**comment** | **str** | Comment. | [optional] 
**coordinates** | [**DeliveryCoordinates**](DeliveryCoordinates.md) | Delivery address coordinates. | [optional] 
**external_cartography_id** | **str** | Address ID in external mapping system. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_point import DeliveryOrderResponsePoint

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponsePoint from a JSON string
delivery_order_response_point_instance = DeliveryOrderResponsePoint.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponsePoint.to_json())

# convert the object into a dict
delivery_order_response_point_dict = delivery_order_response_point_instance.to_dict()
# create an instance of DeliveryOrderResponsePoint from a dict
delivery_order_response_point_from_dict = DeliveryOrderResponsePoint.from_dict(delivery_order_response_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


