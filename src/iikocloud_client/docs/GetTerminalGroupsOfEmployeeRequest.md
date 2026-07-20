# GetTerminalGroupsOfEmployeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** |  | 

## Example

```python
from iikocloud_client.models.get_terminal_groups_of_employee_request import GetTerminalGroupsOfEmployeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTerminalGroupsOfEmployeeRequest from a JSON string
get_terminal_groups_of_employee_request_instance = GetTerminalGroupsOfEmployeeRequest.from_json(json)
# print the JSON string representation of the object
print(GetTerminalGroupsOfEmployeeRequest.to_json())

# convert the object into a dict
get_terminal_groups_of_employee_request_dict = get_terminal_groups_of_employee_request_instance.to_dict()
# create an instance of GetTerminalGroupsOfEmployeeRequest from a dict
get_terminal_groups_of_employee_request_from_dict = GetTerminalGroupsOfEmployeeRequest.from_dict(get_terminal_groups_of_employee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


