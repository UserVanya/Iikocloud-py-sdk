# NomenclatureProductModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers** | [**List[NomenclatureProductChildModifier]**](NomenclatureProductChildModifier.md) | Child modifiers | [optional] 
**child_modifiers_have_min_max_restrictions** | **bool** | Child modifiers have their own min/max amount restrictions | [optional] 
**default_amount** | **int** | Default modifier amount | [optional] 
**free_of_charge_amount** | **int** | Free-of-charge modifier amount | [optional] 
**hide_if_default_amount** | **bool** | Hide the modifier when the default amount is selected | [optional] 
**maximum_amount** | **int** | Maximum modifier amount | [optional] 
**minimum_amount** | **int** | Minimum modifier amount | [optional] 
**modifier_id** | **UUID** | UUID of the modifier | [optional] 
**required** | **bool** | Required modifier | [optional] 
**splittable** | **bool** | The modifier can be split between dish portions | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_modifier import NomenclatureProductModifier

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductModifier from a JSON string
nomenclature_product_modifier_instance = NomenclatureProductModifier.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductModifier.to_json())

# convert the object into a dict
nomenclature_product_modifier_dict = nomenclature_product_modifier_instance.to_dict()
# create an instance of NomenclatureProductModifier from a dict
nomenclature_product_modifier_from_dict = NomenclatureProductModifier.from_dict(nomenclature_product_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


