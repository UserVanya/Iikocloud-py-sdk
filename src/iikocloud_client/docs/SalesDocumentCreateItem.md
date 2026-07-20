# SalesDocumentCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**store** | **str** | Store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.sales_document_create_item import SalesDocumentCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesDocumentCreateItem from a JSON string
sales_document_create_item_instance = SalesDocumentCreateItem.from_json(json)
# print the JSON string representation of the object
print(SalesDocumentCreateItem.to_json())

# convert the object into a dict
sales_document_create_item_dict = sales_document_create_item_instance.to_dict()
# create an instance of SalesDocumentCreateItem from a dict
sales_document_create_item_from_dict = SalesDocumentCreateItem.from_dict(sales_document_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


