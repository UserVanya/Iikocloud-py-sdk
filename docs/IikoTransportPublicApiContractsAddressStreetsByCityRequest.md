# IikoTransportPublicApiContractsAddressStreetsByCityRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID details of which have to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**city_id** | **UUID** | City ID. | 
**include_deleted** | **bool** | Include deleted streets in response. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_city_request import IikoTransportPublicApiContractsAddressStreetsByCityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreetsByCityRequest from a JSON string
iiko_transport_public_api_contracts_address_streets_by_city_request_instance = IikoTransportPublicApiContractsAddressStreetsByCityRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreetsByCityRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_streets_by_city_request_dict = iiko_transport_public_api_contracts_address_streets_by_city_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreetsByCityRequest from a dict
iiko_transport_public_api_contracts_address_streets_by_city_request_from_dict = IikoTransportPublicApiContractsAddressStreetsByCityRequest.from_dict(iiko_transport_public_api_contracts_address_streets_by_city_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


