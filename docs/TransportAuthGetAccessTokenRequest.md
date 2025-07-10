# TransportAuthGetAccessTokenRequest

Authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_login** | **str** | API key. It is set in iikoWeb. | 

## Example

```python
from iiko_cloud_client.models.transport_auth_get_access_token_request import TransportAuthGetAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAuthGetAccessTokenRequest from a JSON string
transport_auth_get_access_token_request_instance = TransportAuthGetAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(TransportAuthGetAccessTokenRequest.to_json())

# convert the object into a dict
transport_auth_get_access_token_request_dict = transport_auth_get_access_token_request_instance.to_dict()
# create an instance of TransportAuthGetAccessTokenRequest from a dict
transport_auth_get_access_token_request_from_dict = TransportAuthGetAccessTokenRequest.from_dict(transport_auth_get_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


