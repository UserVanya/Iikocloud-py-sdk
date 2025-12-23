# TerminalsTerminalGroup

DTO containing terminal groups details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organization ID to which delivery group belongs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**name** | **str** | Terminal group name. | 
**address** | **str** | Group address. Not used. | 
**time_zone** | **str** | Terminal group time zone. | 
**external_data** | [**List[CommonExternalData]**](CommonExternalData.md) | Terminal group external data. | [optional] 

## Example

```python
from iikocloud_client.models.terminals_terminal_group import TerminalsTerminalGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsTerminalGroup from a JSON string
terminals_terminal_group_instance = TerminalsTerminalGroup.from_json(json)
# print the JSON string representation of the object
print(TerminalsTerminalGroup.to_json())

# convert the object into a dict
terminals_terminal_group_dict = terminals_terminal_group_instance.to_dict()
# create an instance of TerminalsTerminalGroup from a dict
terminals_terminal_group_from_dict = TerminalsTerminalGroup.from_dict(terminals_terminal_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


