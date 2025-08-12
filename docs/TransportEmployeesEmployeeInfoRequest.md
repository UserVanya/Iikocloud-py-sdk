# TransportEmployeesEmployeeInfoRequest

Request for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**id** | **str** | Employee ID. | 

## Example

```python
from iikocloud_client.models.transport_employees_employee_info_request import TransportEmployeesEmployeeInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeeInfoRequest from a JSON string
transport_employees_employee_info_request_instance = TransportEmployeesEmployeeInfoRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeeInfoRequest.to_json())

# convert the object into a dict
transport_employees_employee_info_request_dict = transport_employees_employee_info_request_instance.to_dict()
# create an instance of TransportEmployeesEmployeeInfoRequest from a dict
transport_employees_employee_info_request_from_dict = TransportEmployeesEmployeeInfoRequest.from_dict(transport_employees_employee_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


