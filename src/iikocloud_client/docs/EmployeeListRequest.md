# EmployeeListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** | Requested response fields: &#x60;id&#x60;, &#x60;code&#x60;, &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;middleName&#x60;, &#x60;name&#x60;, &#x60;phone&#x60;, &#x60;email&#x60;, &#x60;cardNumber&#x60;, &#x60;mainRoleId&#x60;, &#x60;roleIds&#x60;, &#x60;isSystem&#x60;, &#x60;isFired&#x60;, &#x60;hireDate&#x60;, &#x60;fireDate&#x60;, &#x60;note&#x60;, &#x60;mainOrganizationId&#x60;, &#x60;organizationIds&#x60;, &#x60;responsibleForOrganizationIds&#x60;.  If empty - returns 4 fields only: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;code&#x60;, &#x60;isFired&#x60;.  | [optional] 
**filters** | [**List[EmployeesFilter]**](EmployeesFilter.md) | Filter fields. | 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 

## Example

```python
from iikocloud_client.models.employee_list_request import EmployeeListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeListRequest from a JSON string
employee_list_request_instance = EmployeeListRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeeListRequest.to_json())

# convert the object into a dict
employee_list_request_dict = employee_list_request_instance.to_dict()
# create an instance of EmployeeListRequest from a dict
employee_list_request_from_dict = EmployeeListRequest.from_dict(employee_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


