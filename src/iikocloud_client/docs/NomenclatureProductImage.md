# NomenclatureProductImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_at** | **str** | Certificate expiry date. ISO 8601 | [optional] 
**image_id** | **UUID** | Quality certificate image | [optional] 
**start_at** | **str** | Certificate start date. ISO 8601 | [optional] 
**type** | **str** | Certificate type | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_image import NomenclatureProductImage

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductImage from a JSON string
nomenclature_product_image_instance = NomenclatureProductImage.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductImage.to_json())

# convert the object into a dict
nomenclature_product_image_dict = nomenclature_product_image_instance.to_dict()
# create an instance of NomenclatureProductImage from a dict
nomenclature_product_image_from_dict = NomenclatureProductImage.from_dict(nomenclature_product_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


