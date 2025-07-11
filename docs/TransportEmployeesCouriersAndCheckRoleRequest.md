# TransportEmployeesCouriersAndCheckRoleRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | List of organizations.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**roles_to_check** | **List[str]** | Employee&#39;s roles for check. The short name of employee&#39;s position. | 

## Example

```python
from iikocloud_client.models.transport_employees_couriers_and_check_role_request import TransportEmployeesCouriersAndCheckRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCouriersAndCheckRoleRequest from a JSON string
transport_employees_couriers_and_check_role_request_instance = TransportEmployeesCouriersAndCheckRoleRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCouriersAndCheckRoleRequest.to_json())

# convert the object into a dict
transport_employees_couriers_and_check_role_request_dict = transport_employees_couriers_and_check_role_request_instance.to_dict()
# create an instance of TransportEmployeesCouriersAndCheckRoleRequest from a dict
transport_employees_couriers_and_check_role_request_from_dict = TransportEmployeesCouriersAndCheckRoleRequest.from_dict(transport_employees_couriers_and_check_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


