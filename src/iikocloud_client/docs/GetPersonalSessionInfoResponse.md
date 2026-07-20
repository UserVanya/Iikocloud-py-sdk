# GetPersonalSessionInfoResponse

Personal session info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**error** | **str** | Error details. | [optional] 
**is_session_opened** | **bool** | Is personal session opened. | [optional] 

## Example

```python
from iikocloud_client.models.get_personal_session_info_response import GetPersonalSessionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonalSessionInfoResponse from a JSON string
get_personal_session_info_response_instance = GetPersonalSessionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetPersonalSessionInfoResponse.to_json())

# convert the object into a dict
get_personal_session_info_response_dict = get_personal_session_info_response_instance.to_dict()
# create an instance of GetPersonalSessionInfoResponse from a dict
get_personal_session_info_response_from_dict = GetPersonalSessionInfoResponse.from_dict(get_personal_session_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


