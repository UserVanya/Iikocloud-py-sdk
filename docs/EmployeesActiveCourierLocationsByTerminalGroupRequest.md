# EmployeesActiveCourierLocationsByTerminalGroupRequest

Request for list of active drivers for front group with ID = *TerminalGroupId*.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | iikoFront terminals group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.employees_active_courier_locations_by_terminal_group_request import EmployeesActiveCourierLocationsByTerminalGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesActiveCourierLocationsByTerminalGroupRequest from a JSON string
employees_active_courier_locations_by_terminal_group_request_instance = EmployeesActiveCourierLocationsByTerminalGroupRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesActiveCourierLocationsByTerminalGroupRequest.to_json())

# convert the object into a dict
employees_active_courier_locations_by_terminal_group_request_dict = employees_active_courier_locations_by_terminal_group_request_instance.to_dict()
# create an instance of EmployeesActiveCourierLocationsByTerminalGroupRequest from a dict
employees_active_courier_locations_by_terminal_group_request_from_dict = EmployeesActiveCourierLocationsByTerminalGroupRequest.from_dict(employees_active_courier_locations_by_terminal_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


