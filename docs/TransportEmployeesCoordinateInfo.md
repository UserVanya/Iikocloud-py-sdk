# TransportEmployeesCoordinateInfo

DTO of map coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**server_timestamp** | **int** | Time of coordinate saving on server in the Unix timestamp format. | 

## Example

```python
from iikocloud_client.models.transport_employees_coordinate_info import TransportEmployeesCoordinateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCoordinateInfo from a JSON string
transport_employees_coordinate_info_instance = TransportEmployeesCoordinateInfo.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCoordinateInfo.to_json())

# convert the object into a dict
transport_employees_coordinate_info_dict = transport_employees_coordinate_info_instance.to_dict()
# create an instance of TransportEmployeesCoordinateInfo from a dict
transport_employees_coordinate_info_from_dict = TransportEmployeesCoordinateInfo.from_dict(transport_employees_coordinate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


