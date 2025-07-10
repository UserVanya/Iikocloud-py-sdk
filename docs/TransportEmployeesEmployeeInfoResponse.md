# TransportEmployeesEmployeeInfoResponse

Response for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**employee_info** | [**TransportEmployeesEmployeeInfo**](TransportEmployeesEmployeeInfo.md) | Employee info. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_employee_info_response import TransportEmployeesEmployeeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeeInfoResponse from a JSON string
transport_employees_employee_info_response_instance = TransportEmployeesEmployeeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeeInfoResponse.to_json())

# convert the object into a dict
transport_employees_employee_info_response_dict = transport_employees_employee_info_response_instance.to_dict()
# create an instance of TransportEmployeesEmployeeInfoResponse from a dict
transport_employees_employee_info_response_from_dict = TransportEmployeesEmployeeInfoResponse.from_dict(transport_employees_employee_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


