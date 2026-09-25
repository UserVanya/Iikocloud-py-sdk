# EmployeesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter by. Possible values: &#x60;id&#x60;, &#x60;code&#x60;, &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;middleName&#x60;, &#x60;phone&#x60;, &#x60;email&#x60;, &#x60;mainRoleId&#x60;, &#x60;organizationId&#x60;, &#x60;isFired&#x60; | [optional] 
**value** | **str** | Filter value | [optional] 

## Example

```python
from iikocloud_client.models.employees_filter import EmployeesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesFilter from a JSON string
employees_filter_instance = EmployeesFilter.from_json(json)
# print the JSON string representation of the object
print(EmployeesFilter.to_json())

# convert the object into a dict
employees_filter_dict = employees_filter_instance.to_dict()
# create an instance of EmployeesFilter from a dict
employees_filter_from_dict = EmployeesFilter.from_dict(employees_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


