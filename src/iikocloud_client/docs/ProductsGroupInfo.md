# ProductsGroupInfo

DTO for outside transferring of external menu group details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Additional information. | [optional] 
**code** | **str** | SKU. | [optional] 
**description** | **str** | Description. | [optional] 
**id** | **UUID** | ID. | 
**image_links** | **List[str]** | Links to images. | 
**is_deleted** | **bool** | Is-Deleted attribute. | [optional] 
**is_group_modifier** | **bool** | Is group modifier attribute.  * true - group modifier.  * false - external menu group. | 
**is_included_in_menu** | **bool** | On-the-menu attribute. | 
**name** | **str** | Name. | 
**order** | **int** | Group&#39;s order (priority) in menu. | 
**parent_group** | **UUID** | Parent group. | [optional] 
**seo_description** | **str** | SEO description for client. | [optional] 
**seo_keywords** | **str** | SEO key words. | [optional] 
**seo_text** | **str** | SEO text for robots. | [optional] 
**seo_title** | **str** | SEO header. | [optional] 
**tags** | **List[str]** | Tags. | [optional] 

## Example

```python
from iikocloud_client.models.products_group_info import ProductsGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsGroupInfo from a JSON string
products_group_info_instance = ProductsGroupInfo.from_json(json)
# print the JSON string representation of the object
print(ProductsGroupInfo.to_json())

# convert the object into a dict
products_group_info_dict = products_group_info_instance.to_dict()
# create an instance of ProductsGroupInfo from a dict
products_group_info_from_dict = ProductsGroupInfo.from_dict(products_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


