# IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest

Close personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**employee_id** | **UUID** | Employee ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_close_personal_session_request import IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest from a JSON string
iiko_transport_public_api_contracts_employees_close_personal_session_request_instance = IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_close_personal_session_request_dict = iiko_transport_public_api_contracts_employees_close_personal_session_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest from a dict
iiko_transport_public_api_contracts_employees_close_personal_session_request_from_dict = IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest.from_dict(iiko_transport_public_api_contracts_employees_close_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


