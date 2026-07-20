# ClosePersonalSessionRequest

Close personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | Employee ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.close_personal_session_request import ClosePersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClosePersonalSessionRequest from a JSON string
close_personal_session_request_instance = ClosePersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(ClosePersonalSessionRequest.to_json())

# convert the object into a dict
close_personal_session_request_dict = close_personal_session_request_instance.to_dict()
# create an instance of ClosePersonalSessionRequest from a dict
close_personal_session_request_from_dict = ClosePersonalSessionRequest.from_dict(close_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


