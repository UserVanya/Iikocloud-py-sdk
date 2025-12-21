# IikoTransportPublicApiContractsAddressStreetById

Street by id response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Street id. | 
**classifier_id** | **str** | Street classifierId. | [optional] 
**city_id** | **UUID** | City id. | 
**city_name** | **str** | City name. | 
**street_name** | **str** | Street name. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_street_by_id import IikoTransportPublicApiContractsAddressStreetById

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreetById from a JSON string
iiko_transport_public_api_contracts_address_street_by_id_instance = IikoTransportPublicApiContractsAddressStreetById.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreetById.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_street_by_id_dict = iiko_transport_public_api_contracts_address_street_by_id_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreetById from a dict
iiko_transport_public_api_contracts_address_street_by_id_from_dict = IikoTransportPublicApiContractsAddressStreetById.from_dict(iiko_transport_public_api_contracts_address_street_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


