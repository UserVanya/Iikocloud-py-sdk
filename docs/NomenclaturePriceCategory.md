# NomenclaturePriceCategory

Price category, related to ApiLogin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.nomenclature_price_category import NomenclaturePriceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclaturePriceCategory from a JSON string
nomenclature_price_category_instance = NomenclaturePriceCategory.from_json(json)
# print the JSON string representation of the object
print(NomenclaturePriceCategory.to_json())

# convert the object into a dict
nomenclature_price_category_dict = nomenclature_price_category_instance.to_dict()
# create an instance of NomenclaturePriceCategory from a dict
nomenclature_price_category_from_dict = NomenclaturePriceCategory.from_dict(nomenclature_price_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


