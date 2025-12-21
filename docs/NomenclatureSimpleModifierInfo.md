# NomenclatureSimpleModifierInfo

Modifier details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**default_amount** | **int** | Default quantity. | [optional] 
**min_amount** | **int** | Minimum quantity. | 
**max_amount** | **int** | Maximum quantity. | 
**required** | **bool** | Required availability. | [optional] 
**hide_if_default_amount** | **bool** | Hide if default amount applied. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**splittable** | **bool** | Modifier can be split. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**free_of_charge_amount** | **int** | Free of charge amount. This field is supported since 7.2.4 iikoRMS version. | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_simple_modifier_info import NomenclatureSimpleModifierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureSimpleModifierInfo from a JSON string
nomenclature_simple_modifier_info_instance = NomenclatureSimpleModifierInfo.from_json(json)
# print the JSON string representation of the object
print(NomenclatureSimpleModifierInfo.to_json())

# convert the object into a dict
nomenclature_simple_modifier_info_dict = nomenclature_simple_modifier_info_instance.to_dict()
# create an instance of NomenclatureSimpleModifierInfo from a dict
nomenclature_simple_modifier_info_from_dict = NomenclatureSimpleModifierInfo.from_dict(nomenclature_simple_modifier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


