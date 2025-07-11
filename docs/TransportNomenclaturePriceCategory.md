# TransportNomenclaturePriceCategory

Price category, related to ApiLogin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.transport_nomenclature_price_category import TransportNomenclaturePriceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclaturePriceCategory from a JSON string
transport_nomenclature_price_category_instance = TransportNomenclaturePriceCategory.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclaturePriceCategory.to_json())

# convert the object into a dict
transport_nomenclature_price_category_dict = transport_nomenclature_price_category_instance.to_dict()
# create an instance of TransportNomenclaturePriceCategory from a dict
transport_nomenclature_price_category_from_dict = TransportNomenclaturePriceCategory.from_dict(transport_nomenclature_price_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


