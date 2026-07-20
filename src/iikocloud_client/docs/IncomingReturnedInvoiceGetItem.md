# IncomingReturnedInvoiceGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_factor** | **float** | Write-off factor | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**customs_declaration_number** | **str** | Customs declaration number | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**income_price** | **float** | Cost price at the time of return | [optional] 
**income_sum** | **float** | Cost sum at the time of return | [optional] 
**num** | **int** | Item sequence number | [optional] 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**price_without_vat** | **float** | Price excluding VAT | [optional] 
**producer** | **str** | Manufacturer / importer | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_article** | **str** | Nomenclature article | [optional] 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**store** | **str** | Store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**supplier_product** | **str** | Buyer&#39;s product | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.incoming_returned_invoice_get_item import IncomingReturnedInvoiceGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingReturnedInvoiceGetItem from a JSON string
incoming_returned_invoice_get_item_instance = IncomingReturnedInvoiceGetItem.from_json(json)
# print the JSON string representation of the object
print(IncomingReturnedInvoiceGetItem.to_json())

# convert the object into a dict
incoming_returned_invoice_get_item_dict = incoming_returned_invoice_get_item_instance.to_dict()
# create an instance of IncomingReturnedInvoiceGetItem from a dict
incoming_returned_invoice_get_item_from_dict = IncomingReturnedInvoiceGetItem.from_dict(incoming_returned_invoice_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


