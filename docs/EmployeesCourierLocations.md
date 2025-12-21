# EmployeesCourierLocations

Driver location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **UUID** | Driver ID. | 
**locations** | [**List[EmployeesCoordinateInfo]**](EmployeesCoordinateInfo.md) | List of locations. | 

## Example

```python
from iikocloud_client.models.employees_courier_locations import EmployeesCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesCourierLocations from a JSON string
employees_courier_locations_instance = EmployeesCourierLocations.from_json(json)
# print the JSON string representation of the object
print(EmployeesCourierLocations.to_json())

# convert the object into a dict
employees_courier_locations_dict = employees_courier_locations_instance.to_dict()
# create an instance of EmployeesCourierLocations from a dict
employees_courier_locations_from_dict = EmployeesCourierLocations.from_dict(employees_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


