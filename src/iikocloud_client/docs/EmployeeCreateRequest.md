# EmployeeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number | [optional] 
**code** | **str** | Code | 
**email** | **str** | E-mail | [optional] 
**first_name** | **str** | First name | [optional] 
**hire_date** | **str** | Employee hire date. Can be &#x60;null&#x60; | [optional] 
**last_name** | **str** | Last name | [optional] 
**main_organization_id** | **str** | Identifier (organizationId) of the employee&#39;s main organization | 
**main_role_id** | **str** | Position identifier | [optional] 
**middle_name** | **str** | Middle name | [optional] 
**name** | **str** | Employee name in the system | [optional] 
**note** | **str** | Notes | [optional] 
**organization_ids** | **List[str]** | Identifiers (organizationId) of the employee&#39;s organizations | [optional] 
**phone** | **str** | Phone | [optional] 
**responsible_for_organization_ids** | **List[str]** | Identifiers (organizationId) of the organizations the employee is responsible for | [optional] 

## Example

```python
from iikocloud_client.models.employee_create_request import EmployeeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeCreateRequest from a JSON string
employee_create_request_instance = EmployeeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeCreateRequest.to_json())

# convert the object into a dict
employee_create_request_dict = employee_create_request_instance.to_dict()
# create an instance of EmployeeCreateRequest from a dict
employee_create_request_from_dict = EmployeeCreateRequest.from_dict(employee_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


