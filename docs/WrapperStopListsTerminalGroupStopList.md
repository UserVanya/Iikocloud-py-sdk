# WrapperStopListsTerminalGroupStopList

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[StopListsTerminalGroupStopList]**](StopListsTerminalGroupStopList.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_stop_lists_terminal_group_stop_list import WrapperStopListsTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperStopListsTerminalGroupStopList from a JSON string
wrapper_stop_lists_terminal_group_stop_list_instance = WrapperStopListsTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(WrapperStopListsTerminalGroupStopList.to_json())

# convert the object into a dict
wrapper_stop_lists_terminal_group_stop_list_dict = wrapper_stop_lists_terminal_group_stop_list_instance.to_dict()
# create an instance of WrapperStopListsTerminalGroupStopList from a dict
wrapper_stop_lists_terminal_group_stop_list_from_dict = WrapperStopListsTerminalGroupStopList.from_dict(wrapper_stop_lists_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


