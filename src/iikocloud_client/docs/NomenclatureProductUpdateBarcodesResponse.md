# NomenclatureProductUpdateBarcodesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message | [optional] 
**product_id** | **UUID** | Product ID | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_update_barcodes_response import NomenclatureProductUpdateBarcodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductUpdateBarcodesResponse from a JSON string
nomenclature_product_update_barcodes_response_instance = NomenclatureProductUpdateBarcodesResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductUpdateBarcodesResponse.to_json())

# convert the object into a dict
nomenclature_product_update_barcodes_response_dict = nomenclature_product_update_barcodes_response_instance.to_dict()
# create an instance of NomenclatureProductUpdateBarcodesResponse from a dict
nomenclature_product_update_barcodes_response_from_dict = NomenclatureProductUpdateBarcodesResponse.from_dict(nomenclature_product_update_barcodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


