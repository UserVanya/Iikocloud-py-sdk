# ChangePersonalSessionResponse

Personal session change response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.change_personal_session_response import ChangePersonalSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePersonalSessionResponse from a JSON string
change_personal_session_response_instance = ChangePersonalSessionResponse.from_json(json)
# print the JSON string representation of the object
print(ChangePersonalSessionResponse.to_json())

# convert the object into a dict
change_personal_session_response_dict = change_personal_session_response_instance.to_dict()
# create an instance of ChangePersonalSessionResponse from a dict
change_personal_session_response_from_dict = ChangePersonalSessionResponse.from_dict(change_personal_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


