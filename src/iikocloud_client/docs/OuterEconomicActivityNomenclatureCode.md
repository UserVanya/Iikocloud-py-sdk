# OuterEconomicActivityNomenclatureCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the foreign economic activity commodity code | [optional] 
**is_deleted** | **bool** | Whether the code is soft-deleted | [optional] 
**name** | **str** | Name of the foreign economic activity commodity code | [optional] 
**outer_ean_code** | **str** | Code per the EAEU FEACN (TN VED) classification | [optional] 

## Example

```python
from iikocloud_client.models.outer_economic_activity_nomenclature_code import OuterEconomicActivityNomenclatureCode

# TODO update the JSON string below
json = "{}"
# create an instance of OuterEconomicActivityNomenclatureCode from a JSON string
outer_economic_activity_nomenclature_code_instance = OuterEconomicActivityNomenclatureCode.from_json(json)
# print the JSON string representation of the object
print(OuterEconomicActivityNomenclatureCode.to_json())

# convert the object into a dict
outer_economic_activity_nomenclature_code_dict = outer_economic_activity_nomenclature_code_instance.to_dict()
# create an instance of OuterEconomicActivityNomenclatureCode from a dict
outer_economic_activity_nomenclature_code_from_dict = OuterEconomicActivityNomenclatureCode.from_dict(outer_economic_activity_nomenclature_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


