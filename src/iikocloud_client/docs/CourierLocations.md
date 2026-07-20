# CourierLocations

Driver location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **UUID** | Driver ID. | 
**locations** | [**List[CoordinateInfo]**](CoordinateInfo.md) | List of locations. | 

## Example

```python
from iikocloud_client.models.courier_locations import CourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of CourierLocations from a JSON string
courier_locations_instance = CourierLocations.from_json(json)
# print the JSON string representation of the object
print(CourierLocations.to_json())

# convert the object into a dict
courier_locations_dict = courier_locations_instance.to_dict()
# create an instance of CourierLocations from a dict
courier_locations_from_dict = CourierLocations.from_dict(courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


