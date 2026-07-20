# RmsTerminalGroupItemsResponse

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TerminalGroup]**](TerminalGroup.md) | Items for organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.rms_terminal_group_items_response import RmsTerminalGroupItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RmsTerminalGroupItemsResponse from a JSON string
rms_terminal_group_items_response_instance = RmsTerminalGroupItemsResponse.from_json(json)
# print the JSON string representation of the object
print(RmsTerminalGroupItemsResponse.to_json())

# convert the object into a dict
rms_terminal_group_items_response_dict = rms_terminal_group_items_response_instance.to_dict()
# create an instance of RmsTerminalGroupItemsResponse from a dict
rms_terminal_group_items_response_from_dict = RmsTerminalGroupItemsResponse.from_dict(rms_terminal_group_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


