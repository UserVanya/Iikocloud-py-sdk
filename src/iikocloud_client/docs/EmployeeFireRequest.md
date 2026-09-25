# EmployeeFireRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | List of employee identifiers to fire | 

## Example

```python
from iikocloud_client.models.employee_fire_request import EmployeeFireRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFireRequest from a JSON string
employee_fire_request_instance = EmployeeFireRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeFireRequest.to_json())

# convert the object into a dict
employee_fire_request_dict = employee_fire_request_instance.to_dict()
# create an instance of EmployeeFireRequest from a dict
employee_fire_request_from_dict = EmployeeFireRequest.from_dict(employee_fire_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


