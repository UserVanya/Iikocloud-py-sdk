# ReturnedInvoiceGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**customs_declaration_number** | **str** | Customs declaration number | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**income_price** | **float** |  | [optional] 
**num** | **int** | Item sequence number | [optional] 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**price_without_vat** | **float** | Price excluding VAT | [optional] 
**producer** | **str** | Manufacturer / importer | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_article** | **str** | Nomenclature article | [optional] 
**store** | **str** | Store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**supplier_product** | **str** | Supplier product | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.returned_invoice_get_item import ReturnedInvoiceGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceGetItem from a JSON string
returned_invoice_get_item_instance = ReturnedInvoiceGetItem.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceGetItem.to_json())

# convert the object into a dict
returned_invoice_get_item_dict = returned_invoice_get_item_instance.to_dict()
# create an instance of ReturnedInvoiceGetItem from a dict
returned_invoice_get_item_from_dict = ReturnedInvoiceGetItem.from_dict(returned_invoice_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


