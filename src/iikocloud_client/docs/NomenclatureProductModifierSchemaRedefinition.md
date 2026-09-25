# NomenclatureProductModifierSchemaRedefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers** | [**List[NomenclatureProductChildModifier]**](NomenclatureProductChildModifier.md) | Redefined child modifiers | [optional] 
**default_amount** | **int** | Redefined default amount | [optional] 
**free_of_charge_amount** | **int** | Redefined free-of-charge amount | [optional] 
**maximum_amount** | **int** | Redefined maximum amount. null - no limit | [optional] 
**minimum_amount** | **int** | Redefined minimum amount. null - no limit | [optional] 
**modifier_id** | **UUID** | UUID of the modifier whose schema parameters are redefined | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_modifier_schema_redefinition import NomenclatureProductModifierSchemaRedefinition

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductModifierSchemaRedefinition from a JSON string
nomenclature_product_modifier_schema_redefinition_instance = NomenclatureProductModifierSchemaRedefinition.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductModifierSchemaRedefinition.to_json())

# convert the object into a dict
nomenclature_product_modifier_schema_redefinition_dict = nomenclature_product_modifier_schema_redefinition_instance.to_dict()
# create an instance of NomenclatureProductModifierSchemaRedefinition from a dict
nomenclature_product_modifier_schema_redefinition_from_dict = NomenclatureProductModifierSchemaRedefinition.from_dict(nomenclature_product_modifier_schema_redefinition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


