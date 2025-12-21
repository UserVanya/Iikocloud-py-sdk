# IikoTransportPublicApiContractsAddressCitiesRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**include_deleted** | **bool** | Include deleted cities in response. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_cities_request import IikoTransportPublicApiContractsAddressCitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressCitiesRequest from a JSON string
iiko_transport_public_api_contracts_address_cities_request_instance = IikoTransportPublicApiContractsAddressCitiesRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressCitiesRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_cities_request_dict = iiko_transport_public_api_contracts_address_cities_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressCitiesRequest from a dict
iiko_transport_public_api_contracts_address_cities_request_from_dict = IikoTransportPublicApiContractsAddressCitiesRequest.from_dict(iiko_transport_public_api_contracts_address_cities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


