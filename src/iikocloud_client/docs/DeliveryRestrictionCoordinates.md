# DeliveryRestrictionCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.delivery_restriction_coordinates import DeliveryRestrictionCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionCoordinates from a JSON string
delivery_restriction_coordinates_instance = DeliveryRestrictionCoordinates.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionCoordinates.to_json())

# convert the object into a dict
delivery_restriction_coordinates_dict = delivery_restriction_coordinates_instance.to_dict()
# create an instance of DeliveryRestrictionCoordinates from a dict
delivery_restriction_coordinates_from_dict = DeliveryRestrictionCoordinates.from_dict(delivery_restriction_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


