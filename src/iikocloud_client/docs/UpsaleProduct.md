# UpsaleProduct

Product that suggested to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of product. | [optional] 
**id** | **UUID** | Id of product. | [optional] 

## Example

```python
from iikocloud_client.models.upsale_product import UpsaleProduct

# TODO update the JSON string below
json = "{}"
# create an instance of UpsaleProduct from a JSON string
upsale_product_instance = UpsaleProduct.from_json(json)
# print the JSON string representation of the object
print(UpsaleProduct.to_json())

# convert the object into a dict
upsale_product_dict = upsale_product_instance.to_dict()
# create an instance of UpsaleProduct from a dict
upsale_product_from_dict = UpsaleProduct.from_dict(upsale_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


