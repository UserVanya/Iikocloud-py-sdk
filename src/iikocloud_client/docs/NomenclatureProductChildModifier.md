# NomenclatureProductChildModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers** | [**List[NomenclatureProductChildModifier]**](NomenclatureProductChildModifier.md) | Child modifiers of the next nesting level | [optional] 
**child_modifiers_have_min_max_restrictions** | **bool** | Child modifiers have their own min/max amount restrictions | [optional] 
**default_amount** | **int** | Default modifier amount | [optional] 
**free_of_charge_amount** | **int** | Free-of-charge modifier amount | [optional] 
**hide_if_default_amount** | **bool** | Hide the modifier when the default amount is selected | [optional] 
**maximum_amount** | **int** | Maximum modifier amount. null - no limit | [optional] 
**minimum_amount** | **int** | Minimum modifier amount. null - no limit | [optional] 
**modifier_id** | **UUID** | UUID of the modifier | [optional] 
**required** | **bool** | Required modifier | [optional] 
**splittable** | **bool** | The modifier can be split between dish portions | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_child_modifier import NomenclatureProductChildModifier

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductChildModifier from a JSON string
nomenclature_product_child_modifier_instance = NomenclatureProductChildModifier.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductChildModifier.to_json())

# convert the object into a dict
nomenclature_product_child_modifier_dict = nomenclature_product_child_modifier_instance.to_dict()
# create an instance of NomenclatureProductChildModifier from a dict
nomenclature_product_child_modifier_from_dict = NomenclatureProductChildModifier.from_dict(nomenclature_product_child_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


