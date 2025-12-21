# AuthGetAccessTokenRequest

Authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_login** | **str** | API key. It is set in iikoWeb. | 

## Example

```python
from iikocloud_client.models.auth_get_access_token_request import AuthGetAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthGetAccessTokenRequest from a JSON string
auth_get_access_token_request_instance = AuthGetAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AuthGetAccessTokenRequest.to_json())

# convert the object into a dict
auth_get_access_token_request_dict = auth_get_access_token_request_instance.to_dict()
# create an instance of AuthGetAccessTokenRequest from a dict
auth_get_access_token_request_from_dict = AuthGetAccessTokenRequest.from_dict(auth_get_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


