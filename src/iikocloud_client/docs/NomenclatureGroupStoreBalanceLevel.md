# NomenclatureGroupStoreBalanceLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **UUID** | UUID of the warehouse | 
**value** | **float** | Stock level value. null when valueAssigned &#x3D; false | [optional] 
**value_assigned** | **bool** | true - value is set explicitly and taken from this array; false - taken from defaultMinimum/MaximumStoreBalanceLevel | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_store_balance_level import NomenclatureGroupStoreBalanceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupStoreBalanceLevel from a JSON string
nomenclature_group_store_balance_level_instance = NomenclatureGroupStoreBalanceLevel.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupStoreBalanceLevel.to_json())

# convert the object into a dict
nomenclature_group_store_balance_level_dict = nomenclature_group_store_balance_level_instance.to_dict()
# create an instance of NomenclatureGroupStoreBalanceLevel from a dict
nomenclature_group_store_balance_level_from_dict = NomenclatureGroupStoreBalanceLevel.from_dict(nomenclature_group_store_balance_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


