# EmployeeInfoResponse

Response for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employee_info** | [**EmployeeInfo**](EmployeeInfo.md) | Employee info. | 

## Example

```python
from iikocloud_client.models.employee_info_response import EmployeeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeInfoResponse from a JSON string
employee_info_response_instance = EmployeeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeInfoResponse.to_json())

# convert the object into a dict
employee_info_response_dict = employee_info_response_instance.to_dict()
# create an instance of EmployeeInfoResponse from a dict
employee_info_response_from_dict = EmployeeInfoResponse.from_dict(employee_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


