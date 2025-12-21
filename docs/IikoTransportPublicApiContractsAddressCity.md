# IikoTransportPublicApiContractsAddressCity

City DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | City ID in RMS. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External revision. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**additional_info** | **str** | City additional information. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_city import IikoTransportPublicApiContractsAddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressCity from a JSON string
iiko_transport_public_api_contracts_address_city_instance = IikoTransportPublicApiContractsAddressCity.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressCity.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_city_dict = iiko_transport_public_api_contracts_address_city_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressCity from a dict
iiko_transport_public_api_contracts_address_city_from_dict = IikoTransportPublicApiContractsAddressCity.from_dict(iiko_transport_public_api_contracts_address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


