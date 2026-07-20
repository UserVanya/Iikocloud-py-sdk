# EmployeeDirectoryEntry

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**first_name** | **str** | Name of user. | [optional] 
**id** | **UUID** | Employee ID. | 
**is_deleted** | **bool** | User deletion flag. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**middle_name** | **str** | Second name. | [optional] 

## Example

```python
from iikocloud_client.models.employee_directory_entry import EmployeeDirectoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeDirectoryEntry from a JSON string
employee_directory_entry_instance = EmployeeDirectoryEntry.from_json(json)
# print the JSON string representation of the object
print(EmployeeDirectoryEntry.to_json())

# convert the object into a dict
employee_directory_entry_dict = employee_directory_entry_instance.to_dict()
# create an instance of EmployeeDirectoryEntry from a dict
employee_directory_entry_from_dict = EmployeeDirectoryEntry.from_dict(employee_directory_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


