# EmployeesActiveCourierLocationsResponse

Wrapping object to retrieve list of active courier locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**active_courier_locations** | [**List[WrapperEmployeesActiveCourierLocation]**](WrapperEmployeesActiveCourierLocation.md) | List of courier&#39;s locations. | 

## Example

```python
from iikocloud_client.models.employees_active_courier_locations_response import EmployeesActiveCourierLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesActiveCourierLocationsResponse from a JSON string
employees_active_courier_locations_response_instance = EmployeesActiveCourierLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesActiveCourierLocationsResponse.to_json())

# convert the object into a dict
employees_active_courier_locations_response_dict = employees_active_courier_locations_response_instance.to_dict()
# create an instance of EmployeesActiveCourierLocationsResponse from a dict
employees_active_courier_locations_response_from_dict = EmployeesActiveCourierLocationsResponse.from_dict(employees_active_courier_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


