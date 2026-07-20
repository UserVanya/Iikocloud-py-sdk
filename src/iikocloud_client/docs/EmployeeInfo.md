# EmployeeInfo

Employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_phone** | **str** | Cell phone. | [optional] 
**display_name** | **str** | Display name. | [optional] 
**email** | **str** | Email. | [optional] 
**first_name** | **str** | Name of employee. | [optional] 
**id** | **UUID** | Employee ID. | 
**last_name** | **str** | Last name. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**phone** | **str** | Phone. | [optional] 

## Example

```python
from iikocloud_client.models.employee_info import EmployeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeInfo from a JSON string
employee_info_instance = EmployeeInfo.from_json(json)
# print the JSON string representation of the object
print(EmployeeInfo.to_json())

# convert the object into a dict
employee_info_dict = employee_info_instance.to_dict()
# create an instance of EmployeeInfo from a dict
employee_info_from_dict = EmployeeInfo.from_dict(employee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


