# IikoTransportPublicApiContractsNomenclatureProductCategoryInfo

DTO for outside transferring of product category details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Product category ID. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted attribute. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_product_category_info import IikoTransportPublicApiContractsNomenclatureProductCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureProductCategoryInfo from a JSON string
iiko_transport_public_api_contracts_nomenclature_product_category_info_instance = IikoTransportPublicApiContractsNomenclatureProductCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureProductCategoryInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_product_category_info_dict = iiko_transport_public_api_contracts_nomenclature_product_category_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureProductCategoryInfo from a dict
iiko_transport_public_api_contracts_nomenclature_product_category_info_from_dict = IikoTransportPublicApiContractsNomenclatureProductCategoryInfo.from_dict(iiko_transport_public_api_contracts_nomenclature_product_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


