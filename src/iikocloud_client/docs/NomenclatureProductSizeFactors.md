# NomenclatureProductSizeFactors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | **Dict[str, Dict[str, str]]** | Write-off factor table: key - dish size UUID, value - a map of quantity range lower bound to write-off factor | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_size_factors import NomenclatureProductSizeFactors

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductSizeFactors from a JSON string
nomenclature_product_size_factors_instance = NomenclatureProductSizeFactors.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductSizeFactors.to_json())

# convert the object into a dict
nomenclature_product_size_factors_dict = nomenclature_product_size_factors_instance.to_dict()
# create an instance of NomenclatureProductSizeFactors from a dict
nomenclature_product_size_factors_from_dict = NomenclatureProductSizeFactors.from_dict(nomenclature_product_size_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


