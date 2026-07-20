# RmsTerminalGroupStopListItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TerminalGroupStopList]**](TerminalGroupStopList.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_terminal_group_stop_list_items_response import RmsTerminalGroupStopListItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsTerminalGroupStopListItemsResponse from a JSON string
rms_terminal_group_stop_list_items_response_instance = RmsTerminalGroupStopListItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsTerminalGroupStopListItemsResponse.to_json())

# convert the object into a dict
rms_terminal_group_stop_list_items_response_dict = rms_terminal_group_stop_list_items_response_instance.to_dict()
# create an instance of RmsTerminalGroupStopListItemsResponse from a dict
rms_terminal_group_stop_list_items_response_from_dict = RmsTerminalGroupStopListItemsResponse.from_dict(rms_terminal_group_stop_list_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


