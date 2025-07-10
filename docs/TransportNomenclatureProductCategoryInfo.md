# TransportNomenclatureProductCategoryInfo

DTO for outside transferring of product category details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product category ID. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted attribute. | 

## Example

```python
from iiko_cloud_client.models.transport_nomenclature_product_category_info import TransportNomenclatureProductCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureProductCategoryInfo from a JSON string
transport_nomenclature_product_category_info_instance = TransportNomenclatureProductCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureProductCategoryInfo.to_json())

# convert the object into a dict
transport_nomenclature_product_category_info_dict = transport_nomenclature_product_category_info_instance.to_dict()
# create an instance of TransportNomenclatureProductCategoryInfo from a dict
transport_nomenclature_product_category_info_from_dict = TransportNomenclatureProductCategoryInfo.from_dict(transport_nomenclature_product_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


