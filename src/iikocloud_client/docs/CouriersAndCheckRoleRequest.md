# CouriersAndCheckRoleRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | List of organizations.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**roles_to_check** | **List[str]** | Employee&#39;s roles for check. The short name of employee&#39;s position. | 

## Example

```python
from iikocloud_client.models.couriers_and_check_role_request import CouriersAndCheckRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouriersAndCheckRoleRequest from a JSON string
couriers_and_check_role_request_instance = CouriersAndCheckRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CouriersAndCheckRoleRequest.to_json())

# convert the object into a dict
couriers_and_check_role_request_dict = couriers_and_check_role_request_instance.to_dict()
# create an instance of CouriersAndCheckRoleRequest from a dict
couriers_and_check_role_request_from_dict = CouriersAndCheckRoleRequest.from_dict(couriers_and_check_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


