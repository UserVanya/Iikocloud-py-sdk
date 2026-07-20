# TerminalGroup

DTO containing terminal groups details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Group address. Not used. | 
**external_data** | [**List[CommonExternalData]**](CommonExternalData.md) | Terminal group external data. | [optional] 
**id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**name** | **str** | Terminal group name. | 
**organization_id** | **UUID** | Organization ID to which delivery group belongs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**pos_version** | **str** | Version of the iikoFront. | [optional] 
**time_zone** | **str** | Terminal group time zone. | 

## Example

```python
from iikocloud_client.models.terminal_group import TerminalGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroup from a JSON string
terminal_group_instance = TerminalGroup.from_json(json)
# print the JSON string representation of the object
print(TerminalGroup.to_json())

# convert the object into a dict
terminal_group_dict = terminal_group_instance.to_dict()
# create an instance of TerminalGroup from a dict
terminal_group_from_dict = TerminalGroup.from_dict(terminal_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


