# IncomingInvoice


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
**delivery_on_time** | **bool** | On-time delivery flag | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**employee_pass_to_account** | **str** | Charge to employee | [optional] 
**incoming_date** | **str** | Incoming document date (YYYY-MM-DD) | [optional] 
**incoming_document_number** | **str** | Incoming external document number | [optional] 
**internal_outgoing_invoice_id** | **str** | Associated outgoing invoice identifier (GUID) | [optional] 
**invoice** | **str** | Invoice number | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[IncomingInvoiceItem]**](IncomingInvoiceItem.md) | List of document items | [optional] 
**matches_to_the_order** | **bool** | Matches the order | [optional] 
**number** | **str** | Document number | [optional] 
**payment_date** | **str** | Payment date (YYYY-MM-DD) | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**transport_invoice_number** | **str** | Transport invoice number | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_invoice import IncomingInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoice from a JSON string
incoming_invoice_instance = IncomingInvoice.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoice.to_json())

# convert the object into a dict
incoming_invoice_dict = incoming_invoice_instance.to_dict()
# create an instance of IncomingInvoice from a dict
incoming_invoice_from_dict = IncomingInvoice.from_dict(incoming_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


