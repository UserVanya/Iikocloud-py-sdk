# EmployeeRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee identifier | 

## Example

```python
from iikocloud_client.models.employee_restore_request import EmployeeRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeRestoreRequest from a JSON string
employee_restore_request_instance = EmployeeRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeRestoreRequest.to_json())

# convert the object into a dict
employee_restore_request_dict = employee_restore_request_instance.to_dict()
# create an instance of EmployeeRestoreRequest from a dict
employee_restore_request_from_dict = EmployeeRestoreRequest.from_dict(employee_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


