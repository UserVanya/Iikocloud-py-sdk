# OutgoingInvoiceRequestItem


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
**store** | **str** | Store identifier (GUID) | 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_invoice_request_item import OutgoingInvoiceRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingInvoiceRequestItem from a JSON string
outgoing_invoice_request_item_instance = OutgoingInvoiceRequestItem.from_json(json)
# print the JSON string representation of the object
print(OutgoingInvoiceRequestItem.to_json())

# convert the object into a dict
outgoing_invoice_request_item_dict = outgoing_invoice_request_item_instance.to_dict()
# create an instance of OutgoingInvoiceRequestItem from a dict
outgoing_invoice_request_item_from_dict = OutgoingInvoiceRequestItem.from_dict(outgoing_invoice_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


