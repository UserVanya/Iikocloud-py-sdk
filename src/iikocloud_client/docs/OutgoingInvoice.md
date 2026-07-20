# OutgoingInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**default_store** | **str** | Default store identifier (GUID) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**internal_incoming_invoice_id** | **str** | Associated incoming invoice identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[OutgoingInvoiceItem]**](OutgoingInvoiceItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**payment_date** | **str** | Payment date (YYYY-MM-DD) | [optional] 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_invoice import OutgoingInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingInvoice from a JSON string
outgoing_invoice_instance = OutgoingInvoice.from_json(json)
# print the JSON string representation of the object
print(OutgoingInvoice.to_json())

# convert the object into a dict
outgoing_invoice_dict = outgoing_invoice_instance.to_dict()
# create an instance of OutgoingInvoice from a dict
outgoing_invoice_from_dict = OutgoingInvoice.from_dict(outgoing_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


