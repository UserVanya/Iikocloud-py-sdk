# EmployeeInfoRequest

Request for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Employee ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.employee_info_request import EmployeeInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeInfoRequest from a JSON string
employee_info_request_instance = EmployeeInfoRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeInfoRequest.to_json())

# convert the object into a dict
employee_info_request_dict = employee_info_request_instance.to_dict()
# create an instance of EmployeeInfoRequest from a dict
employee_info_request_from_dict = EmployeeInfoRequest.from_dict(employee_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


