# IncomingReturnedInvoiceCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_factor** | **float** | publicapi.model.incoming_returned_invoice_item.amountFactor | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**customs_declaration_number** | **str** | Customs declaration number | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**income_price** | **float** | Cost price at the time of return | [optional] 
**income_sum** | **float** | Cost sum at the time of return | [optional] 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 
**store** | **str** | Store identifier (GUID) | 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**supplier_product** | **str** | Buyer&#39;s product | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.incoming_returned_invoice_create_item import IncomingReturnedInvoiceCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingReturnedInvoiceCreateItem from a JSON string
incoming_returned_invoice_create_item_instance = IncomingReturnedInvoiceCreateItem.from_json(json)
# print the JSON string representation of the object
print(IncomingReturnedInvoiceCreateItem.to_json())

# convert the object into a dict
incoming_returned_invoice_create_item_dict = incoming_returned_invoice_create_item_instance.to_dict()
# create an instance of IncomingReturnedInvoiceCreateItem from a dict
incoming_returned_invoice_create_item_from_dict = IncomingReturnedInvoiceCreateItem.from_dict(incoming_returned_invoice_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


