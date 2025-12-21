# WrapperTerminalsTerminalGroup

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[TerminalsTerminalGroup]**](TerminalsTerminalGroup.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_terminals_terminal_group import WrapperTerminalsTerminalGroup

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperTerminalsTerminalGroup from a JSON string
wrapper_terminals_terminal_group_instance = WrapperTerminalsTerminalGroup.from_json(json)
# print the JSON string representation of the object
print(WrapperTerminalsTerminalGroup.to_json())

# convert the object into a dict
wrapper_terminals_terminal_group_dict = wrapper_terminals_terminal_group_instance.to_dict()
# create an instance of WrapperTerminalsTerminalGroup from a dict
wrapper_terminals_terminal_group_from_dict = WrapperTerminalsTerminalGroup.from_dict(wrapper_terminals_terminal_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


