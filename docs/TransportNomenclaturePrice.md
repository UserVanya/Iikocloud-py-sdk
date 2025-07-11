# TransportNomenclaturePrice

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
from iikocloud_client.models.transport_nomenclature_price import TransportNomenclaturePrice

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclaturePrice from a JSON string
transport_nomenclature_price_instance = TransportNomenclaturePrice.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclaturePrice.to_json())

# convert the object into a dict
transport_nomenclature_price_dict = transport_nomenclature_price_instance.to_dict()
# create an instance of TransportNomenclaturePrice from a dict
transport_nomenclature_price_from_dict = TransportNomenclaturePrice.from_dict(transport_nomenclature_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


