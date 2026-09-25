# NomenclatureProductDayTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | **int** | Time in minutes from the start of the day (0–1439) | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_day_time import NomenclatureProductDayTime

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductDayTime from a JSON string
nomenclature_product_day_time_instance = NomenclatureProductDayTime.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductDayTime.to_json())

# convert the object into a dict
nomenclature_product_day_time_dict = nomenclature_product_day_time_instance.to_dict()
# create an instance of NomenclatureProductDayTime from a dict
nomenclature_product_day_time_from_dict = NomenclatureProductDayTime.from_dict(nomenclature_product_day_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


