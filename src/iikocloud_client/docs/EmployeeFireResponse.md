# EmployeeFireResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fired_ids** | **List[str]** | List of fired employee identifiers | [optional] 

## Example

```python
from iikocloud_client.models.employee_fire_response import EmployeeFireResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFireResponse from a JSON string
employee_fire_response_instance = EmployeeFireResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeeFireResponse.to_json())

# convert the object into a dict
employee_fire_response_dict = employee_fire_response_instance.to_dict()
# create an instance of EmployeeFireResponse from a dict
employee_fire_response_from_dict = EmployeeFireResponse.from_dict(employee_fire_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


