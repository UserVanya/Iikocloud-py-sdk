# TransportNomenclatureSizePrice

Price per item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_id** | **str** | Item size ID. | 
**price** | [**TransportNomenclaturePrice**](TransportNomenclaturePrice.md) | Price per this item size. | 

## Example

```python
from iikocloud_client.models.transport_nomenclature_size_price import TransportNomenclatureSizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureSizePrice from a JSON string
transport_nomenclature_size_price_instance = TransportNomenclatureSizePrice.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureSizePrice.to_json())

# convert the object into a dict
transport_nomenclature_size_price_dict = transport_nomenclature_size_price_instance.to_dict()
# create an instance of TransportNomenclatureSizePrice from a dict
transport_nomenclature_size_price_from_dict = TransportNomenclatureSizePrice.from_dict(transport_nomenclature_size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


