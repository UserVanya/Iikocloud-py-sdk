# IikoTransportPublicApiContractsNomenclatureProductsGroupInfo

DTO for outside transferring of external menu group details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_links** | **List[str]** | Links to images. | 
**parent_group** | **UUID** | Parent group. | [optional] 
**order** | **int** | Group&#39;s order (priority) in menu. | 
**is_included_in_menu** | **bool** | On-the-menu attribute. | 
**is_group_modifier** | **bool** | Is group modifier attribute.  * true - group modifier.  * false - external menu group. | 
**id** | **UUID** | ID. | 
**code** | **str** | SKU. | [optional] 
**name** | **str** | Name. | 
**description** | **str** | Description. | [optional] 
**additional_info** | **str** | Additional information. | [optional] 
**tags** | **List[str]** | Tags. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | [optional] 
**seo_description** | **str** | SEO description for client. | [optional] 
**seo_text** | **str** | SEO text for robots. | [optional] 
**seo_keywords** | **str** | SEO key words. | [optional] 
**seo_title** | **str** | SEO header. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_products_group_info import IikoTransportPublicApiContractsNomenclatureProductsGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureProductsGroupInfo from a JSON string
iiko_transport_public_api_contracts_nomenclature_products_group_info_instance = IikoTransportPublicApiContractsNomenclatureProductsGroupInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureProductsGroupInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_products_group_info_dict = iiko_transport_public_api_contracts_nomenclature_products_group_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureProductsGroupInfo from a dict
iiko_transport_public_api_contracts_nomenclature_products_group_info_from_dict = IikoTransportPublicApiContractsNomenclatureProductsGroupInfo.from_dict(iiko_transport_public_api_contracts_nomenclature_products_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


