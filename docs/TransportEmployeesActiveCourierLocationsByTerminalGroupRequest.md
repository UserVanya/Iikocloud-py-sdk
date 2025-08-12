# TransportEmployeesActiveCourierLocationsByTerminalGroupRequest

Request for list of active drivers for front group with ID = *TerminalGroupId*.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **str** | iikoFront terminals group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_employees_active_courier_locations_by_terminal_group_request import TransportEmployeesActiveCourierLocationsByTerminalGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesActiveCourierLocationsByTerminalGroupRequest from a JSON string
transport_employees_active_courier_locations_by_terminal_group_request_instance = TransportEmployeesActiveCourierLocationsByTerminalGroupRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesActiveCourierLocationsByTerminalGroupRequest.to_json())

# convert the object into a dict
transport_employees_active_courier_locations_by_terminal_group_request_dict = transport_employees_active_courier_locations_by_terminal_group_request_instance.to_dict()
# create an instance of TransportEmployeesActiveCourierLocationsByTerminalGroupRequest from a dict
transport_employees_active_courier_locations_by_terminal_group_request_from_dict = TransportEmployeesActiveCourierLocationsByTerminalGroupRequest.from_dict(transport_employees_active_courier_locations_by_terminal_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


