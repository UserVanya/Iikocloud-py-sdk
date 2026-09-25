# NomenclatureProductUpdateBarcodesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcodes** | [**List[NomenclatureProductBarcode]**](NomenclatureProductBarcode.md) | Barcodes | 
**product_id** | **UUID** | Product ID | 

## Example

```python
from iikocloud_client.models.nomenclature_product_update_barcodes_request import NomenclatureProductUpdateBarcodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductUpdateBarcodesRequest from a JSON string
nomenclature_product_update_barcodes_request_instance = NomenclatureProductUpdateBarcodesRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductUpdateBarcodesRequest.to_json())

# convert the object into a dict
nomenclature_product_update_barcodes_request_dict = nomenclature_product_update_barcodes_request_instance.to_dict()
# create an instance of NomenclatureProductUpdateBarcodesRequest from a dict
nomenclature_product_update_barcodes_request_from_dict = NomenclatureProductUpdateBarcodesRequest.from_dict(nomenclature_product_update_barcodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


