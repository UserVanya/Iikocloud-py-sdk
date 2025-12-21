# NomenclatureGroupModifierInfo

Information on group of modifiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**min_amount** | **int** | Minimum quantity. | 
**max_amount** | **int** | Maximum quantity. | 
**required** | **bool** | Required availability. | 
**child_modifiers_have_min_max_restrictions** | **bool** | Presence of max/min quantity limitations of child modifiers. | [optional] 
**child_modifiers** | [**List[NomenclatureChildModifierInfo]**](NomenclatureChildModifierInfo.md) | List of child modifiers. | 
**hide_if_default_amount** | **bool** | Hide if the amount is by default. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**default_amount** | **int** | Amount by default. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**splittable** | **bool** | Modifier can be split. This field is supported since 7.2.4 iikoRMS version. | [optional] 
**free_of_charge_amount** | **int** | Free amount. This field is supported since 7.2.4 iikoRMS version. | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_modifier_info import NomenclatureGroupModifierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupModifierInfo from a JSON string
nomenclature_group_modifier_info_instance = NomenclatureGroupModifierInfo.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupModifierInfo.to_json())

# convert the object into a dict
nomenclature_group_modifier_info_dict = nomenclature_group_modifier_info_instance.to_dict()
# create an instance of NomenclatureGroupModifierInfo from a dict
nomenclature_group_modifier_info_from_dict = NomenclatureGroupModifierInfo.from_dict(nomenclature_group_modifier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


