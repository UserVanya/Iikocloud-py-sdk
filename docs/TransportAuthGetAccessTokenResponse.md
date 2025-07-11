# TransportAuthGetAccessTokenResponse

Response to authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**token** | **str** | Authentication token. The standard token lifetime is 1 hour. | 

## Example

```python
from iikocloud_client.models.transport_auth_get_access_token_response import TransportAuthGetAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAuthGetAccessTokenResponse from a JSON string
transport_auth_get_access_token_response_instance = TransportAuthGetAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(TransportAuthGetAccessTokenResponse.to_json())

# convert the object into a dict
transport_auth_get_access_token_response_dict = transport_auth_get_access_token_response_instance.to_dict()
# create an instance of TransportAuthGetAccessTokenResponse from a dict
transport_auth_get_access_token_response_from_dict = TransportAuthGetAccessTokenResponse.from_dict(transport_auth_get_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


