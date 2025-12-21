# EmployeesCoordinateInfo

DTO of map coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**server_timestamp** | **int** | Time of coordinate saving on server in the Unix timestamp format. | 

## Example

```python
from iikocloud_client.models.employees_coordinate_info import EmployeesCoordinateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesCoordinateInfo from a JSON string
employees_coordinate_info_instance = EmployeesCoordinateInfo.from_json(json)
# print the JSON string representation of the object
print(EmployeesCoordinateInfo.to_json())

# convert the object into a dict
employees_coordinate_info_dict = employees_coordinate_info_instance.to_dict()
# create an instance of EmployeesCoordinateInfo from a dict
employees_coordinate_info_from_dict = EmployeesCoordinateInfo.from_dict(employees_coordinate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


