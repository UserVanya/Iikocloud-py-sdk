# NomenclatureProductRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[NomenclatureProductRateInterval]**](NomenclatureProductRateInterval.md) | Time intervals the rate is active | [optional] 
**service_rate** | **str** | Rate charge per unit of time | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_rate import NomenclatureProductRate

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductRate from a JSON string
nomenclature_product_rate_instance = NomenclatureProductRate.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductRate.to_json())

# convert the object into a dict
nomenclature_product_rate_dict = nomenclature_product_rate_instance.to_dict()
# create an instance of NomenclatureProductRate from a dict
nomenclature_product_rate_from_dict = NomenclatureProductRate.from_dict(nomenclature_product_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


