# IikoTransportPublicApiContractsTerminalsTerminalGroup

DTO containing terminal groups details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **UUID** | Organization ID to which delivery group belongs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**name** | **str** | Terminal group name. | 
**address** | **str** | Group address. Not used. | 
**time_zone** | **str** | Terminal group time zone. | 
**external_data** | [**List[IikoTransportPublicApiContractsCommonExternalData]**](IikoTransportPublicApiContractsCommonExternalData.md) | Terminal group external data. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_group import IikoTransportPublicApiContractsTerminalsTerminalGroup

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroup from a JSON string
iiko_transport_public_api_contracts_terminals_terminal_group_instance = IikoTransportPublicApiContractsTerminalsTerminalGroup.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsTerminalGroup.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_terminal_group_dict = iiko_transport_public_api_contracts_terminals_terminal_group_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroup from a dict
iiko_transport_public_api_contracts_terminals_terminal_group_from_dict = IikoTransportPublicApiContractsTerminalsTerminalGroup.from_dict(iiko_transport_public_api_contracts_terminals_terminal_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


