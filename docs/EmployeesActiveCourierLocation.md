# EmployeesActiveCourierLocation

Courier's location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **UUID** | Employee ID. | [optional] 
**last_active_latitude** | **float** | Latitude. | [optional] 
**last_active_longitude** | **float** | Longitude. | [optional] 
**last_active_client_date** | **str** | Client date and time. | [optional] 

## Example

```python
from iikocloud_client.models.employees_active_courier_location import EmployeesActiveCourierLocation

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesActiveCourierLocation from a JSON string
employees_active_courier_location_instance = EmployeesActiveCourierLocation.from_json(json)
# print the JSON string representation of the object
print(EmployeesActiveCourierLocation.to_json())

# convert the object into a dict
employees_active_courier_location_dict = employees_active_courier_location_instance.to_dict()
# create an instance of EmployeesActiveCourierLocation from a dict
employees_active_courier_location_from_dict = EmployeesActiveCourierLocation.from_dict(employees_active_courier_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


