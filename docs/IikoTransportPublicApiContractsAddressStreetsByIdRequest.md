# IikoTransportPublicApiContractsAddressStreetsByIdRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization Id. | 
**ids** | **List[UUID]** | Street Ids. | [optional] 
**classifier_ids** | **List[str]** | Street classifierIds. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_streets_by_id_request import IikoTransportPublicApiContractsAddressStreetsByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressStreetsByIdRequest from a JSON string
iiko_transport_public_api_contracts_address_streets_by_id_request_instance = IikoTransportPublicApiContractsAddressStreetsByIdRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressStreetsByIdRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_streets_by_id_request_dict = iiko_transport_public_api_contracts_address_streets_by_id_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressStreetsByIdRequest from a dict
iiko_transport_public_api_contracts_address_streets_by_id_request_from_dict = IikoTransportPublicApiContractsAddressStreetsByIdRequest.from_dict(iiko_transport_public_api_contracts_address_streets_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


