# IikoTransportPublicApiContractsNomenclatureNomenclatureRequest

Request for stock list by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**start_revision** | **int** | The revision (version) of the menu saved on the integration side.  Use &#x60;0&#x60; for the first request for each organization. In every subsequent request,  the &#x60;startRevision&#x60; field should contain the value of the &#x60;revision&#x60; field received  in the response to the previous request. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_nomenclature_request import IikoTransportPublicApiContractsNomenclatureNomenclatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureNomenclatureRequest from a JSON string
iiko_transport_public_api_contracts_nomenclature_nomenclature_request_instance = IikoTransportPublicApiContractsNomenclatureNomenclatureRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureNomenclatureRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_nomenclature_request_dict = iiko_transport_public_api_contracts_nomenclature_nomenclature_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureNomenclatureRequest from a dict
iiko_transport_public_api_contracts_nomenclature_nomenclature_request_from_dict = IikoTransportPublicApiContractsNomenclatureNomenclatureRequest.from_dict(iiko_transport_public_api_contracts_nomenclature_nomenclature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


