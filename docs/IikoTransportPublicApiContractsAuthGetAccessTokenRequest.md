# IikoTransportPublicApiContractsAuthGetAccessTokenRequest

Authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_login** | **str** | API key. It is set in iikoWeb. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_auth_get_access_token_request import IikoTransportPublicApiContractsAuthGetAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAuthGetAccessTokenRequest from a JSON string
iiko_transport_public_api_contracts_auth_get_access_token_request_instance = IikoTransportPublicApiContractsAuthGetAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAuthGetAccessTokenRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_auth_get_access_token_request_dict = iiko_transport_public_api_contracts_auth_get_access_token_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAuthGetAccessTokenRequest from a dict
iiko_transport_public_api_contracts_auth_get_access_token_request_from_dict = IikoTransportPublicApiContractsAuthGetAccessTokenRequest.from_dict(iiko_transport_public_api_contracts_auth_get_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


