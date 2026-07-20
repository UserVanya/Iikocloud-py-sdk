# SalesDocumentGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**amount_factor** | **float** |  | [optional] 
**amount_unit** | **str** |  | [optional] 
**container_id** | **str** |  | [optional] 
**discount_sum** | **float** |  | [optional] 
**num** | **int** |  | [optional] 
**price** | **float** |  | [optional] 
**price_without_vat** | **float** |  | [optional] 
**product** | **str** |  | [optional] 
**product_article** | **str** |  | [optional] 
**product_size** | **str** |  | [optional] 
**store** | **str** |  | [optional] 
**sum** | **float** |  | [optional] 
**sum_without_vat** | **float** |  | [optional] 
**vat_percent** | **float** |  | [optional] 

## Example

```python
from iikocloud_client.models.sales_document_get_item import SalesDocumentGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesDocumentGetItem from a JSON string
sales_document_get_item_instance = SalesDocumentGetItem.from_json(json)
# print the JSON string representation of the object
print(SalesDocumentGetItem.to_json())

# convert the object into a dict
sales_document_get_item_dict = sales_document_get_item_instance.to_dict()
# create an instance of SalesDocumentGetItem from a dict
sales_document_get_item_from_dict = SalesDocumentGetItem.from_dict(sales_document_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


