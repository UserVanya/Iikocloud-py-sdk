# NomenclaturePrice

Price per this item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_price** | **float** | Current price. | 
**is_included_in_menu** | **bool** | Is on the menu. | 
**next_price** | **float** | New price | [optional] 
**next_included_in_menu** | **bool** | Will be on the menu in the future. | 
**next_date_price** | **str** | New price validity start date (Local for the terminal). | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_price import NomenclaturePrice

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclaturePrice from a JSON string
nomenclature_price_instance = NomenclaturePrice.from_json(json)
# print the JSON string representation of the object
print(NomenclaturePrice.to_json())

# convert the object into a dict
nomenclature_price_dict = nomenclature_price_instance.to_dict()
# create an instance of NomenclaturePrice from a dict
nomenclature_price_from_dict = NomenclaturePrice.from_dict(nomenclature_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


