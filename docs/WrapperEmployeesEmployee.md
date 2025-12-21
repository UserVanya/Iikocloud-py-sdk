# WrapperEmployeesEmployee

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[EmployeesEmployee]**](EmployeesEmployee.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_employees_employee import WrapperEmployeesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperEmployeesEmployee from a JSON string
wrapper_employees_employee_instance = WrapperEmployeesEmployee.from_json(json)
# print the JSON string representation of the object
print(WrapperEmployeesEmployee.to_json())

# convert the object into a dict
wrapper_employees_employee_dict = wrapper_employees_employee_instance.to_dict()
# create an instance of WrapperEmployeesEmployee from a dict
wrapper_employees_employee_from_dict = WrapperEmployeesEmployee.from_dict(wrapper_employees_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


