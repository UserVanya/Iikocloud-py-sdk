# OpenPersonalSessionRequest

Open personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | Employee ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**role_id** | **UUID** | Employee role ID.                Must be null if the restaurant doesn&#39;t use roles, otherwise not-null role must be specified. | [optional] 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.open_personal_session_request import OpenPersonalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPersonalSessionRequest from a JSON string
open_personal_session_request_instance = OpenPersonalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(OpenPersonalSessionRequest.to_json())

# convert the object into a dict
open_personal_session_request_dict = open_personal_session_request_instance.to_dict()
# create an instance of OpenPersonalSessionRequest from a dict
open_personal_session_request_from_dict = OpenPersonalSessionRequest.from_dict(open_personal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


