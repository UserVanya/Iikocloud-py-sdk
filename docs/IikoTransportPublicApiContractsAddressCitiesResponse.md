# IikoTransportPublicApiContractsAddressCitiesResponse

Service response with list of cities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**cities** | [**List[RmsItemsResponseWrapperAddressCity]**](RmsItemsResponseWrapperAddressCity.md) | List of cities. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_cities_response import IikoTransportPublicApiContractsAddressCitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressCitiesResponse from a JSON string
iiko_transport_public_api_contracts_address_cities_response_instance = IikoTransportPublicApiContractsAddressCitiesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressCitiesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_cities_response_dict = iiko_transport_public_api_contracts_address_cities_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressCitiesResponse from a dict
iiko_transport_public_api_contracts_address_cities_response_from_dict = IikoTransportPublicApiContractsAddressCitiesResponse.from_dict(iiko_transport_public_api_contracts_address_cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


