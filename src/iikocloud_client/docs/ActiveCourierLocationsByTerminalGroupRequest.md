# ActiveCourierLocationsByTerminalGroupRequest

Request for list of active drivers for front group with ID = *TerminalGroupId*.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | iikoFront terminals group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.active_courier_locations_by_terminal_group_request import ActiveCourierLocationsByTerminalGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveCourierLocationsByTerminalGroupRequest from a JSON string
active_courier_locations_by_terminal_group_request_instance = ActiveCourierLocationsByTerminalGroupRequest.from_json(json)
# print the JSON string representation of the object
print(ActiveCourierLocationsByTerminalGroupRequest.to_json())

# convert the object into a dict
active_courier_locations_by_terminal_group_request_dict = active_courier_locations_by_terminal_group_request_instance.to_dict()
# create an instance of ActiveCourierLocationsByTerminalGroupRequest from a dict
active_courier_locations_by_terminal_group_request_from_dict = ActiveCourierLocationsByTerminalGroupRequest.from_dict(active_courier_locations_by_terminal_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


