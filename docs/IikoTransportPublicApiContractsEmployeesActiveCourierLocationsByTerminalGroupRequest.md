# IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest

Request for list of active drivers for front group with ID = *TerminalGroupId*.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | iikoFront terminals group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request import IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest from a JSON string
iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request_instance = IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request_dict = iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest from a dict
iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request_from_dict = IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest.from_dict(iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


