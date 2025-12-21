# IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest

Open personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**employee_id** | **UUID** | Employee ID. | 
**role_id** | **UUID** | Employee role ID.                Must be null if the restaurant doesn&#39;t use roles, otherwise not-null role must be specified. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_open_personal_session_request import IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest from a JSON string
iiko_transport_public_api_contracts_employees_open_personal_session_request_instance = IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_open_personal_session_request_dict = iiko_transport_public_api_contracts_employees_open_personal_session_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest from a dict
iiko_transport_public_api_contracts_employees_open_personal_session_request_from_dict = IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest.from_dict(iiko_transport_public_api_contracts_employees_open_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


