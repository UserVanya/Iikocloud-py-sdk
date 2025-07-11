# TransportNomenclatureProductsGroupInfo

DTO for outside transferring of external menu group details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_links** | **List[str]** | Links to images. | 
**parent_group** | **str** | Parent group. | [optional] 
**order** | **int** | Group&#39;s order (priority) in menu. | 
**is_included_in_menu** | **bool** | On-the-menu attribute. | 
**is_group_modifier** | **bool** | Is group modifier attribute.  * true - group modifier.  * false - external menu group. | 
**id** | **str** | ID. | 
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
from iikocloud_client.models.transport_nomenclature_products_group_info import TransportNomenclatureProductsGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureProductsGroupInfo from a JSON string
transport_nomenclature_products_group_info_instance = TransportNomenclatureProductsGroupInfo.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureProductsGroupInfo.to_json())

# convert the object into a dict
transport_nomenclature_products_group_info_dict = transport_nomenclature_products_group_info_instance.to_dict()
# create an instance of TransportNomenclatureProductsGroupInfo from a dict
transport_nomenclature_products_group_info_from_dict = TransportNomenclatureProductsGroupInfo.from_dict(transport_nomenclature_products_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


