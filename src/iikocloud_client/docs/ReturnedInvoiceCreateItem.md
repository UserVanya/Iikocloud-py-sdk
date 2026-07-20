# ReturnedInvoiceCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**customs_declaration_number** | **str** | Customs declaration number | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**store** | **str** | Store identifier (GUID) | 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**supplier_product** | **str** | Supplier product | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.returned_invoice_create_item import ReturnedInvoiceCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceCreateItem from a JSON string
returned_invoice_create_item_instance = ReturnedInvoiceCreateItem.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceCreateItem.to_json())

# convert the object into a dict
returned_invoice_create_item_dict = returned_invoice_create_item_instance.to_dict()
# create an instance of ReturnedInvoiceCreateItem from a dict
returned_invoice_create_item_from_dict = ReturnedInvoiceCreateItem.from_dict(returned_invoice_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


