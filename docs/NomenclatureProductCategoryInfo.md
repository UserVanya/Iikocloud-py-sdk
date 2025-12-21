# NomenclatureProductCategoryInfo

DTO for outside transferring of product category details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Product category ID. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted attribute. | 

## Example

```python
from iikocloud_client.models.nomenclature_product_category_info import NomenclatureProductCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductCategoryInfo from a JSON string
nomenclature_product_category_info_instance = NomenclatureProductCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductCategoryInfo.to_json())

# convert the object into a dict
nomenclature_product_category_info_dict = nomenclature_product_category_info_instance.to_dict()
# create an instance of NomenclatureProductCategoryInfo from a dict
nomenclature_product_category_info_from_dict = NomenclatureProductCategoryInfo.from_dict(nomenclature_product_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


