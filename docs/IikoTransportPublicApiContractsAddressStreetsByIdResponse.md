# IikoTransportPublicApiContractsAddressStreetsByIdResponse

Streets by ids response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streets** | [**List[IikoTransportPublicApiContractsAddressStreetById]**](IikoTransportPublicApiContractsAddressStreetById.md) | Found streets. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_id_response import IikoTransportPublicApiContractsAddressStreetsByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreetsByIdResponse from a JSON string
iiko_transport_public_api_contracts_address_streets_by_id_response_instance = IikoTransportPublicApiContractsAddressStreetsByIdResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreetsByIdResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_streets_by_id_response_dict = iiko_transport_public_api_contracts_address_streets_by_id_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreetsByIdResponse from a dict
iiko_transport_public_api_contracts_address_streets_by_id_response_from_dict = IikoTransportPublicApiContractsAddressStreetsByIdResponse.from_dict(iiko_transport_public_api_contracts_address_streets_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


