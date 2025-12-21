# IikoTransportPublicApiContractsNomenclatureNomenclatureResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**groups** | [**List[IikoTransportPublicApiContractsNomenclatureProductsGroupInfo]**](IikoTransportPublicApiContractsNomenclatureProductsGroupInfo.md) | Stock list group. | 
**product_categories** | [**List[IikoTransportPublicApiContractsNomenclatureProductCategoryInfo]**](IikoTransportPublicApiContractsNomenclatureProductCategoryInfo.md) | Menu item category. | 
**products** | [**List[IikoTransportPublicApiContractsNomenclatureProductInfo]**](IikoTransportPublicApiContractsNomenclatureProductInfo.md) | Menu items and modifiers. | 
**sizes** | [**List[IikoTransportPublicApiContractsNomenclatureSize]**](IikoTransportPublicApiContractsNomenclatureSize.md) | Item sizes. | 
**revision** | **int** | The revison (version) of the menu recevied in the response of the request.  This value should be saved by the integration and passed in the &#x60;startRevision&#x60; field  of the next menu request. If the values in &#x60;revision&#x60; and &#x60;startRevision&#x60; are the same,  it means there have been no changes to the menu since the previous request.  In this case, the &#x60;groups&#x60;, &#x60;productCategories&#x60;, &#x60;products&#x60; and &#x60;sizes&#x60; fields  will not contain any data. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_nomenclature_response import IikoTransportPublicApiContractsNomenclatureNomenclatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureNomenclatureResponse from a JSON string
iiko_transport_public_api_contracts_nomenclature_nomenclature_response_instance = IikoTransportPublicApiContractsNomenclatureNomenclatureResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureNomenclatureResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_nomenclature_response_dict = iiko_transport_public_api_contracts_nomenclature_nomenclature_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureNomenclatureResponse from a dict
iiko_transport_public_api_contracts_nomenclature_nomenclature_response_from_dict = IikoTransportPublicApiContractsNomenclatureNomenclatureResponse.from_dict(iiko_transport_public_api_contracts_nomenclature_nomenclature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


