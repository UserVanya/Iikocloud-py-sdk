# TransportEmployeesClosePersonalSessionRequest

Close personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Delivery group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**employee_id** | **str** | Employee ID. | 

## Example

```python
from iikocloud_client.models.transport_employees_close_personal_session_request import TransportEmployeesClosePersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesClosePersonalSessionRequest from a JSON string
transport_employees_close_personal_session_request_instance = TransportEmployeesClosePersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesClosePersonalSessionRequest.to_json())

# convert the object into a dict
transport_employees_close_personal_session_request_dict = transport_employees_close_personal_session_request_instance.to_dict()
# create an instance of TransportEmployeesClosePersonalSessionRequest from a dict
transport_employees_close_personal_session_request_from_dict = TransportEmployeesClosePersonalSessionRequest.from_dict(transport_employees_close_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


