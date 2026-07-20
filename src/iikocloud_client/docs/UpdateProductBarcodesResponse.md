# UpdateProductBarcodesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message | [optional] 
**product_id** | **str** | Product ID | [optional] 

## Example

```python
from iikocloud_client.models.update_product_barcodes_response import UpdateProductBarcodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductBarcodesResponse from a JSON string
update_product_barcodes_response_instance = UpdateProductBarcodesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateProductBarcodesResponse.to_json())

# convert the object into a dict
update_product_barcodes_response_dict = update_product_barcodes_response_instance.to_dict()
# create an instance of UpdateProductBarcodesResponse from a dict
update_product_barcodes_response_from_dict = UpdateProductBarcodesResponse.from_dict(update_product_barcodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


