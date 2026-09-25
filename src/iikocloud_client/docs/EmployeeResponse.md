# EmployeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number | [optional] 
**code** | **str** | Code | [optional] 
**email** | **str** | E-mail | [optional] 
**fire_date** | **str** | Employee fire date. If &#x60;null&#x60;, the employee is not fired | [optional] 
**first_name** | **str** | First name | [optional] 
**hire_date** | **str** | Employee hire date. Can be &#x60;null&#x60; | [optional] 
**id** | **str** | Employee identifier | [optional] 
**is_fired** | **bool** | Flag indicating that the employee is fired. If &#x60;true&#x60; — the employee is fired | [optional] 
**is_system** | **bool** | Flag indicating that the employee is a system employee. If &#x60;true&#x60; — the employee is a system employee | [optional] 
**last_name** | **str** | Last name | [optional] 
**main_organization_id** | **str** | Identifier (organizationId) of the employee&#39;s main organization | [optional] 
**main_role_id** | **str** | Position identifier | [optional] 
**middle_name** | **str** | Middle name | [optional] 
**name** | **str** | Employee name in the system | [optional] 
**note** | **str** | Notes | [optional] 
**organization_ids** | **List[str]** | Identifiers (organizationId) of the employee&#39;s organizations | [optional] 
**phone** | **str** | Phone | [optional] 
**responsible_for_organization_ids** | **List[str]** | Identifiers (organizationId) of the organizations the employee is responsible for | [optional] 
**role_ids** | **List[str]** | Employee position identifiers | [optional] 

## Example

```python
from iikocloud_client.models.employee_response import EmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeResponse from a JSON string
employee_response_instance = EmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeResponse.to_json())

# convert the object into a dict
employee_response_dict = employee_response_instance.to_dict()
# create an instance of EmployeeResponse from a dict
employee_response_from_dict = EmployeeResponse.from_dict(employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


