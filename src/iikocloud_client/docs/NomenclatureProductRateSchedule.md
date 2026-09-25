# NomenclatureProductRateSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[NomenclatureProductRate]**](NomenclatureProductRate.md) | List of time-pay service rates | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_rate_schedule import NomenclatureProductRateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductRateSchedule from a JSON string
nomenclature_product_rate_schedule_instance = NomenclatureProductRateSchedule.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductRateSchedule.to_json())

# convert the object into a dict
nomenclature_product_rate_schedule_dict = nomenclature_product_rate_schedule_instance.to_dict()
# create an instance of NomenclatureProductRateSchedule from a dict
nomenclature_product_rate_schedule_from_dict = NomenclatureProductRateSchedule.from_dict(nomenclature_product_rate_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


