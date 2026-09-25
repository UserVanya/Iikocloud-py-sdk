# EmployeeGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee identifier | 

## Example

```python
from iikocloud_client.models.employee_get_request import EmployeeGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeGetRequest from a JSON string
employee_get_request_instance = EmployeeGetRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeGetRequest.to_json())

# convert the object into a dict
employee_get_request_dict = employee_get_request_instance.to_dict()
# create an instance of EmployeeGetRequest from a dict
employee_get_request_from_dict = EmployeeGetRequest.from_dict(employee_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


