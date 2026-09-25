# TerminalListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_anonymous** | **bool** | Include anonymous terminals. Default value: &#x60;false&#x60; | [optional] 
**organization_id** | **UUID** | Organization identifier (GUID) | 
**search** | **str** | Filter by terminal name | [optional] 

## Example

```python
from iikocloud_client.models.terminal_list_request import TerminalListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalListRequest from a JSON string
terminal_list_request_instance = TerminalListRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalListRequest.to_json())

# convert the object into a dict
terminal_list_request_dict = terminal_list_request_instance.to_dict()
# create an instance of TerminalListRequest from a dict
terminal_list_request_from_dict = TerminalListRequest.from_dict(terminal_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


