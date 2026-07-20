# RmsEmployeeWithCheckedRoleItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmployeeWithCheckedRole]**](EmployeeWithCheckedRole.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_employee_with_checked_role_items_response import RmsEmployeeWithCheckedRoleItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsEmployeeWithCheckedRoleItemsResponse from a JSON string
rms_employee_with_checked_role_items_response_instance = RmsEmployeeWithCheckedRoleItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsEmployeeWithCheckedRoleItemsResponse.to_json())

# convert the object into a dict
rms_employee_with_checked_role_items_response_dict = rms_employee_with_checked_role_items_response_instance.to_dict()
# create an instance of RmsEmployeeWithCheckedRoleItemsResponse from a dict
rms_employee_with_checked_role_items_response_from_dict = RmsEmployeeWithCheckedRoleItemsResponse.from_dict(rms_employee_with_checked_role_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


