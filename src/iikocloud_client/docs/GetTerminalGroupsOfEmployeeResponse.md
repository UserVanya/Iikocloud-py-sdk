# GetTerminalGroupsOfEmployeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_ids** | **List[UUID]** |  | 

## Example

```python
from iikocloud_client.models.get_terminal_groups_of_employee_response import GetTerminalGroupsOfEmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTerminalGroupsOfEmployeeResponse from a JSON string
get_terminal_groups_of_employee_response_instance = GetTerminalGroupsOfEmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(GetTerminalGroupsOfEmployeeResponse.to_json())

# convert the object into a dict
get_terminal_groups_of_employee_response_dict = get_terminal_groups_of_employee_response_instance.to_dict()
# create an instance of GetTerminalGroupsOfEmployeeResponse from a dict
get_terminal_groups_of_employee_response_from_dict = GetTerminalGroupsOfEmployeeResponse.from_dict(get_terminal_groups_of_employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


