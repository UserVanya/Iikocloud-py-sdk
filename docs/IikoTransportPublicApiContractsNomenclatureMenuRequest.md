# IikoTransportPublicApiContractsNomenclatureMenuRequest

Request for menu by id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_menu_id** | **str** | External menu id                Can be obtained by &#x60;api/2/menu&#x60; operation. | 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**price_category_id** | **str** | Price category id.                Can be obtained by &#x60;api/2/menu&#x60; operation. | [optional] 
**version** | **int** | Version of the result data model. | [optional] 
**language** | **str** | Language of the external menu. | [optional] 
**async_mode** | **bool** | Async Mode. | [optional] 
**start_revision** | **int** | Start revision. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_menu_request import IikoTransportPublicApiContractsNomenclatureMenuRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureMenuRequest from a JSON string
iiko_transport_public_api_contracts_nomenclature_menu_request_instance = IikoTransportPublicApiContractsNomenclatureMenuRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureMenuRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_menu_request_dict = iiko_transport_public_api_contracts_nomenclature_menu_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureMenuRequest from a dict
iiko_transport_public_api_contracts_nomenclature_menu_request_from_dict = IikoTransportPublicApiContractsNomenclatureMenuRequest.from_dict(iiko_transport_public_api_contracts_nomenclature_menu_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


