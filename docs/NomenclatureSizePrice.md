# NomenclatureSizePrice

Price per item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_id** | **UUID** | Item size ID. | 
**price** | [**NomenclaturePrice**](NomenclaturePrice.md) | Price per this item size. | 

## Example

```python
from iikocloud_client.models.nomenclature_size_price import NomenclatureSizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureSizePrice from a JSON string
nomenclature_size_price_instance = NomenclatureSizePrice.from_json(json)
# print the JSON string representation of the object
print(NomenclatureSizePrice.to_json())

# convert the object into a dict
nomenclature_size_price_dict = nomenclature_size_price_instance.to_dict()
# create an instance of NomenclatureSizePrice from a dict
nomenclature_size_price_from_dict = NomenclatureSizePrice.from_dict(nomenclature_size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


