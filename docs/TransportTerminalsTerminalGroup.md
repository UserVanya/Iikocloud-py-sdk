# TransportTerminalsTerminalGroup

DTO containing terminal groups details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Delivery group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organization ID to which delivery group belongs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**name** | **str** | Terminal group name. | 
**address** | **str** | Group address. Not used. | 
**time_zone** | **str** | Terminal group time zone. | 
**external_data** | [**List[TransportCommonExternalData]**](TransportCommonExternalData.md) | Terminal group external data. | [optional] 

## Example

```python
from iikocloud_client.models.transport_terminals_terminal_group import TransportTerminalsTerminalGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsTerminalGroup from a JSON string
transport_terminals_terminal_group_instance = TransportTerminalsTerminalGroup.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsTerminalGroup.to_json())

# convert the object into a dict
transport_terminals_terminal_group_dict = transport_terminals_terminal_group_instance.to_dict()
# create an instance of TransportTerminalsTerminalGroup from a dict
transport_terminals_terminal_group_from_dict = TransportTerminalsTerminalGroup.from_dict(transport_terminals_terminal_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


