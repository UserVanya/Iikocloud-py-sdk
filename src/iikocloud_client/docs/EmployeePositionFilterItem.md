# EmployeePositionFilterItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name for filtering | [optional] 
**op** | **str** | Operation (\&quot;eq\&quot;, \&quot;ne\&quot;, \&quot;gt\&quot;, \&quot;gte\&quot;, \&quot;lt\&quot;, \&quot;lte\&quot;, \&quot;in\&quot;, \&quot;nin\&quot;, \&quot;like\&quot;, \&quot;blank\&quot;, \&quot;notblank\&quot;) | [optional] 
**value** | **object** | Value for filtering by the field | [optional] 
**values** | **List[object]** | Values for multi-value filtering (\&quot;in\&quot;, \&quot;nin\&quot;) | [optional] 

## Example

```python
from iikocloud_client.models.employee_position_filter_item import EmployeePositionFilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeePositionFilterItem from a JSON string
employee_position_filter_item_instance = EmployeePositionFilterItem.from_json(json)
# print the JSON string representation of the object
print(EmployeePositionFilterItem.to_json())

# convert the object into a dict
employee_position_filter_item_dict = employee_position_filter_item_instance.to_dict()
# create an instance of EmployeePositionFilterItem from a dict
employee_position_filter_item_from_dict = EmployeePositionFilterItem.from_dict(employee_position_filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


