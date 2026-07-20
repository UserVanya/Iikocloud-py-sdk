# DeliveryCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.delivery_coordinates import DeliveryCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryCoordinates from a JSON string
delivery_coordinates_instance = DeliveryCoordinates.from_json(json)
# print the JSON string representation of the object
print(DeliveryCoordinates.to_json())

# convert the object into a dict
delivery_coordinates_dict = delivery_coordinates_instance.to_dict()
# create an instance of DeliveryCoordinates from a dict
delivery_coordinates_from_dict = DeliveryCoordinates.from_dict(delivery_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


