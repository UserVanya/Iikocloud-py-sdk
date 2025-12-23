# TerminalsTerminalGroupsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**include_disabled** | **bool** | Attribute that shows that response contains disabled terminal groups. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.terminals_terminal_groups_request import TerminalsTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsTerminalGroupsRequest from a JSON string
terminals_terminal_groups_request_instance = TerminalsTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalsTerminalGroupsRequest.to_json())

# convert the object into a dict
terminals_terminal_groups_request_dict = terminals_terminal_groups_request_instance.to_dict()
# create an instance of TerminalsTerminalGroupsRequest from a dict
terminals_terminal_groups_request_from_dict = TerminalsTerminalGroupsRequest.from_dict(terminals_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


