# IncomingInvoiceRequestItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_amount** | **float** | Actual quantity | [optional] 
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**customs_declaration_number** | **str** | Customs declaration number | [optional] 
**is_additional_expense** | **bool** | Is additional expense | [optional] 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**store** | **str** | Store identifier (GUID) | 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**supplier_product** | **str** | Supplier product | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.incoming_invoice_request_item import IncomingInvoiceRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoiceRequestItem from a JSON string
incoming_invoice_request_item_instance = IncomingInvoiceRequestItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoiceRequestItem.to_json())

# convert the object into a dict
incoming_invoice_request_item_dict = incoming_invoice_request_item_instance.to_dict()
# create an instance of IncomingInvoiceRequestItem from a dict
incoming_invoice_request_item_from_dict = IncomingInvoiceRequestItem.from_dict(incoming_invoice_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


