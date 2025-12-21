# IikoTransportPublicApiContractsAuthGetAccessTokenResponse

Response to authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**token** | **str** | Authentication token. The standard token lifetime is 1 hour. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_auth_get_access_token_response import IikoTransportPublicApiContractsAuthGetAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAuthGetAccessTokenResponse from a JSON string
iiko_transport_public_api_contracts_auth_get_access_token_response_instance = IikoTransportPublicApiContractsAuthGetAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAuthGetAccessTokenResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_auth_get_access_token_response_dict = iiko_transport_public_api_contracts_auth_get_access_token_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAuthGetAccessTokenResponse from a dict
iiko_transport_public_api_contracts_auth_get_access_token_response_from_dict = IikoTransportPublicApiContractsAuthGetAccessTokenResponse.from_dict(iiko_transport_public_api_contracts_auth_get_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


