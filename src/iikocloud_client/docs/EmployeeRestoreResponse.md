# EmployeeRestoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restored_ids** | **List[str]** | List of restored employee identifiers | [optional] 

## Example

```python
from iikocloud_client.models.employee_restore_response import EmployeeRestoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeRestoreResponse from a JSON string
employee_restore_response_instance = EmployeeRestoreResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeRestoreResponse.to_json())

# convert the object into a dict
employee_restore_response_dict = employee_restore_response_instance.to_dict()
# create an instance of EmployeeRestoreResponse from a dict
employee_restore_response_from_dict = EmployeeRestoreResponse.from_dict(employee_restore_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


