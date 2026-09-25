# NomenclatureProductRateInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | [**NomenclatureProductDayTime**](NomenclatureProductDayTime.md) | Start of the rate&#39;s active interval | [optional] 
**day_of_week** | **str** | Day of the week the rate is active | [optional] 
**end** | [**NomenclatureProductDayTime**](NomenclatureProductDayTime.md) | End of the rate&#39;s active interval | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_rate_interval import NomenclatureProductRateInterval

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductRateInterval from a JSON string
nomenclature_product_rate_interval_instance = NomenclatureProductRateInterval.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductRateInterval.to_json())

# convert the object into a dict
nomenclature_product_rate_interval_dict = nomenclature_product_rate_interval_instance.to_dict()
# create an instance of NomenclatureProductRateInterval from a dict
nomenclature_product_rate_interval_from_dict = NomenclatureProductRateInterval.from_dict(nomenclature_product_rate_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


