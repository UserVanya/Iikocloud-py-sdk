# IikoTransportPublicApiContractsAddressStreet

Street DTO in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External system revision No. | [optional] 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_street import IikoTransportPublicApiContractsAddressStreet

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreet from a JSON string
iiko_transport_public_api_contracts_address_street_instance = IikoTransportPublicApiContractsAddressStreet.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreet.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_street_dict = iiko_transport_public_api_contracts_address_street_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreet from a dict
iiko_transport_public_api_contracts_address_street_from_dict = IikoTransportPublicApiContractsAddressStreet.from_dict(iiko_transport_public_api_contracts_address_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


