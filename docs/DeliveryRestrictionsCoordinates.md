# DeliveryRestrictionsCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_coordinates import DeliveryRestrictionsCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsCoordinates from a JSON string
delivery_restrictions_coordinates_instance = DeliveryRestrictionsCoordinates.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsCoordinates.to_json())

# convert the object into a dict
delivery_restrictions_coordinates_dict = delivery_restrictions_coordinates_instance.to_dict()
# create an instance of DeliveryRestrictionsCoordinates from a dict
delivery_restrictions_coordinates_from_dict = DeliveryRestrictionsCoordinates.from_dict(delivery_restrictions_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


