# TransportDeliveryRestrictionsCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_coordinates import TransportDeliveryRestrictionsCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsCoordinates from a JSON string
transport_delivery_restrictions_coordinates_instance = TransportDeliveryRestrictionsCoordinates.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsCoordinates.to_json())

# convert the object into a dict
transport_delivery_restrictions_coordinates_dict = transport_delivery_restrictions_coordinates_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsCoordinates from a dict
transport_delivery_restrictions_coordinates_from_dict = TransportDeliveryRestrictionsCoordinates.from_dict(transport_delivery_restrictions_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


