# TransportEmployeesEmployeeInfo

Employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of employee. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Display name. | [optional] 
**email** | **str** | Email. | [optional] 
**phone** | **str** | Phone. | [optional] 
**cell_phone** | **str** | Cell phone. | [optional] 

## Example

```python
from iikocloud_client.models.transport_employees_employee_info import TransportEmployeesEmployeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeeInfo from a JSON string
transport_employees_employee_info_instance = TransportEmployeesEmployeeInfo.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeeInfo.to_json())

# convert the object into a dict
transport_employees_employee_info_dict = transport_employees_employee_info_instance.to_dict()
# create an instance of TransportEmployeesEmployeeInfo from a dict
transport_employees_employee_info_from_dict = TransportEmployeesEmployeeInfo.from_dict(transport_employees_employee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


