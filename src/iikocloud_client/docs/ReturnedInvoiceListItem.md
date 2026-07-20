# ReturnedInvoiceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_stores** | **List[str]** | Write-off locations (UUID array) | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**deleted** | **bool** | Flag indicating that the document is deleted | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**number** | **str** | Document number | [optional] 
**processed** | **bool** | Flag indicating that the document is processed | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.returned_invoice_list_item import ReturnedInvoiceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceListItem from a JSON string
returned_invoice_list_item_instance = ReturnedInvoiceListItem.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceListItem.to_json())

# convert the object into a dict
returned_invoice_list_item_dict = returned_invoice_list_item_instance.to_dict()
# create an instance of ReturnedInvoiceListItem from a dict
returned_invoice_list_item_from_dict = ReturnedInvoiceListItem.from_dict(returned_invoice_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


