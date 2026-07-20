# GetPersonalSessionInfoRequest

Personal session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | Employee ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Delivery group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_personal_session_info_request import GetPersonalSessionInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonalSessionInfoRequest from a JSON string
get_personal_session_info_request_instance = GetPersonalSessionInfoRequest.from_json(json)
# print the JSON string representation of the object
print(GetPersonalSessionInfoRequest.to_json())

# convert the object into a dict
get_personal_session_info_request_dict = get_personal_session_info_request_instance.to_dict()
# create an instance of GetPersonalSessionInfoRequest from a dict
get_personal_session_info_request_from_dict = GetPersonalSessionInfoRequest.from_dict(get_personal_session_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


