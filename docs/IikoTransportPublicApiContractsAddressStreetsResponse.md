# IikoTransportPublicApiContractsAddressStreetsResponse

Service response with list of streets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**streets** | [**List[IikoTransportPublicApiContractsAddressStreet]**](IikoTransportPublicApiContractsAddressStreet.md) | List of streets. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_response import IikoTransportPublicApiContractsAddressStreetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreetsResponse from a JSON string
iiko_transport_public_api_contracts_address_streets_response_instance = IikoTransportPublicApiContractsAddressStreetsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreetsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_streets_response_dict = iiko_transport_public_api_contracts_address_streets_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreetsResponse from a dict
iiko_transport_public_api_contracts_address_streets_response_from_dict = IikoTransportPublicApiContractsAddressStreetsResponse.from_dict(iiko_transport_public_api_contracts_address_streets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


