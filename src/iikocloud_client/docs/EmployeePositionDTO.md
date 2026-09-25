# EmployeePositionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_work_by_substituted_card** | **bool** | Allowed to work with a substituted card | [optional] 
**code** | **str** | Employee position code | [optional] 
**id** | **str** | Employee position identifier (GUID) | [optional] 
**is_deleted** | **bool** | Flag indicating a deleted position | [optional] 
**name** | **str** | Employee position name | [optional] 
**payment_per_hour** | **float** | Hourly payment rate | [optional] 
**schedule_type** | **str** | Schedule type (HOURS, FIXED, SESSION, BYTIME) | [optional] 
**steady_salary** | **float** | Monthly salary amount | [optional] 

## Example

```python
from iikocloud_client.models.employee_position_dto import EmployeePositionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePositionDTO from a JSON string
employee_position_dto_instance = EmployeePositionDTO.from_json(json)
# print the JSON string representation of the object
print(EmployeePositionDTO.to_json())

# convert the object into a dict
employee_position_dto_dict = employee_position_dto_instance.to_dict()
# create an instance of EmployeePositionDTO from a dict
employee_position_dto_from_dict = EmployeePositionDTO.from_dict(employee_position_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


