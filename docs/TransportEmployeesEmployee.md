# TransportEmployeesEmployee

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_employees_employee import TransportEmployeesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployee from a JSON string
transport_employees_employee_instance = TransportEmployeesEmployee.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployee.to_json())

# convert the object into a dict
transport_employees_employee_dict = transport_employees_employee_instance.to_dict()
# create an instance of TransportEmployeesEmployee from a dict
transport_employees_employee_from_dict = TransportEmployeesEmployee.from_dict(transport_employees_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


