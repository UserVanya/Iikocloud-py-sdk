# NomenclatureProductNutritionValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carbohydrate_amount** | **float** | Carbohydrate content, g. | [optional] 
**energy_amount** | **float** | Energy value, kcal | [optional] 
**fat_amount** | **float** | Fat content, g. | [optional] 
**nutrition_components** | **Dict[str, float]** | Components of nutritional value | [optional] 
**organization_ids** | **List[UUID]** | UUIDs of the organizations (structural units) the nutrition value is set for | [optional] 
**product_size_id** | **UUID** | UUID of the dish size. null - for a dish without a size scale. The list of values can be retrieved via the \&quot;Get a list of product sizes\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**protein_amount** | **float** | Protein content, g. | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_nutrition_value import NomenclatureProductNutritionValue

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductNutritionValue from a JSON string
nomenclature_product_nutrition_value_instance = NomenclatureProductNutritionValue.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductNutritionValue.to_json())

# convert the object into a dict
nomenclature_product_nutrition_value_dict = nomenclature_product_nutrition_value_instance.to_dict()
# create an instance of NomenclatureProductNutritionValue from a dict
nomenclature_product_nutrition_value_from_dict = NomenclatureProductNutritionValue.from_dict(nomenclature_product_nutrition_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


