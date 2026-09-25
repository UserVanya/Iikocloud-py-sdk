# EmployeeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number | [optional] 
**code** | **str** | Code | [optional] 
**email** | **str** | E-mail | [optional] 
**first_name** | **str** | First name | [optional] 
**hire_date** | **str** | Employee hire date. Can be &#x60;null&#x60; | [optional] 
**id** | **str** | Employee identifier | 
**last_name** | **str** | Last name | [optional] 
**main_organization_id** | **str** | Identifier (organizationId) of the employee&#39;s main organization | [optional] 
**main_role_id** | **str** | Position identifier | [optional] 
**middle_name** | **str** | Middle name | [optional] 
**name** | **str** | Employee name in the system | [optional] 
**note** | **str** | Notes | [optional] 
**organization_ids** | **List[str]** | Identifiers (organizationId) of the employee&#39;s organizations | [optional] 
**phone** | **str** | Phone | [optional] 
**responsible_for_organization_ids** | **List[str]** | Identifiers (organizationId) of the organizations the employee is responsible for | [optional] 

## Example

```python
from iikocloud_client.models.employee_update_request import EmployeeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeUpdateRequest from a JSON string
employee_update_request_instance = EmployeeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeUpdateRequest.to_json())

# convert the object into a dict
employee_update_request_dict = employee_update_request_instance.to_dict()
# create an instance of EmployeeUpdateRequest from a dict
employee_update_request_from_dict = EmployeeUpdateRequest.from_dict(employee_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


