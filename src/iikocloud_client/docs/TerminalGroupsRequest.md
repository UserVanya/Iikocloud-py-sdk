# TerminalGroupsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_disabled** | **bool** | Attribute that shows that response contains disabled terminal groups. | [optional] 
**organization_ids** | **List[UUID]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.terminal_groups_request import TerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroupsRequest from a JSON string
terminal_groups_request_instance = TerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalGroupsRequest.to_json())

# convert the object into a dict
terminal_groups_request_dict = terminal_groups_request_instance.to_dict()
# create an instance of TerminalGroupsRequest from a dict
terminal_groups_request_from_dict = TerminalGroupsRequest.from_dict(terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


