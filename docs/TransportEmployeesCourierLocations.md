# TransportEmployeesCourierLocations

Driver location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **str** | Driver ID. | 
**locations** | [**List[TransportEmployeesCoordinateInfo]**](TransportEmployeesCoordinateInfo.md) | List of locations. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_courier_locations import TransportEmployeesCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCourierLocations from a JSON string
transport_employees_courier_locations_instance = TransportEmployeesCourierLocations.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCourierLocations.to_json())

# convert the object into a dict
transport_employees_courier_locations_dict = transport_employees_courier_locations_instance.to_dict()
# create an instance of TransportEmployeesCourierLocations from a dict
transport_employees_courier_locations_from_dict = TransportEmployeesCourierLocations.from_dict(transport_employees_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


