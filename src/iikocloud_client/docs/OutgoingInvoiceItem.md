# OutgoingInvoiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_factor** | **float** | Write-off factor | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**num** | **int** | Item sequence number | [optional] 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**price_without_vat** | **float** | Price excluding VAT | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_article** | **str** | Nomenclature article | [optional] 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**store** | **str** | Store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_invoice_item import OutgoingInvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingInvoiceItem from a JSON string
outgoing_invoice_item_instance = OutgoingInvoiceItem.from_json(json)
# print the JSON string representation of the object
print(OutgoingInvoiceItem.to_json())

# convert the object into a dict
outgoing_invoice_item_dict = outgoing_invoice_item_instance.to_dict()
# create an instance of OutgoingInvoiceItem from a dict
outgoing_invoice_item_from_dict = OutgoingInvoiceItem.from_dict(outgoing_invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


