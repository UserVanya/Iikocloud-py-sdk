# DeliveriesCommonCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.deliveries_common_coordinates import DeliveriesCommonCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonCoordinates from a JSON string
deliveries_common_coordinates_instance = DeliveriesCommonCoordinates.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonCoordinates.to_json())

# convert the object into a dict
deliveries_common_coordinates_dict = deliveries_common_coordinates_instance.to_dict()
# create an instance of DeliveriesCommonCoordinates from a dict
deliveries_common_coordinates_from_dict = DeliveriesCommonCoordinates.from_dict(deliveries_common_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


