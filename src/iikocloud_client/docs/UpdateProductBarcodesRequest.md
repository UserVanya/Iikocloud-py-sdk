# UpdateProductBarcodesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcodes** | [**List[BarcodeItem]**](BarcodeItem.md) | Barcodes | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | [optional] 
**product_id** | **str** | Product ID | [optional] 

## Example

```python
from iikocloud_client.models.update_product_barcodes_request import UpdateProductBarcodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductBarcodesRequest from a JSON string
update_product_barcodes_request_instance = UpdateProductBarcodesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProductBarcodesRequest.to_json())

# convert the object into a dict
update_product_barcodes_request_dict = update_product_barcodes_request_instance.to_dict()
# create an instance of UpdateProductBarcodesRequest from a dict
update_product_barcodes_request_from_dict = UpdateProductBarcodesRequest.from_dict(update_product_barcodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


