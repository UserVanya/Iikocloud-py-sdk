# TerminalListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computer_name** | **str** | Terminal host address | [optional] 
**id** | **UUID** | Terminal identifier (UUID) | [optional] 
**is_anonymous** | **bool** | Anonymous terminal flag | [optional] 
**name** | **str** | Terminal name | [optional] 
**restaurant_section_ids** | **List[str]** | Identifiers of the dining-hall sections available to the terminal | [optional] 

## Example

```python
from iikocloud_client.models.terminal_list_item import TerminalListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalListItem from a JSON string
terminal_list_item_instance = TerminalListItem.from_json(json)
# print the JSON string representation of the object
print(TerminalListItem.to_json())

# convert the object into a dict
terminal_list_item_dict = terminal_list_item_instance.to_dict()
# create an instance of TerminalListItem from a dict
terminal_list_item_from_dict = TerminalListItem.from_dict(terminal_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


