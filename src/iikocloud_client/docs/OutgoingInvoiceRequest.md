# OutgoingInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**default_store** | **str** | Default store identifier (GUID) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**internal_incoming_invoice_id** | **str** | Associated incoming invoice identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[OutgoingInvoiceRequestItem]**](OutgoingInvoiceRequestItem.md) | List of document items | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_invoice_request import OutgoingInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingInvoiceRequest from a JSON string
outgoing_invoice_request_instance = OutgoingInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(OutgoingInvoiceRequest.to_json())

# convert the object into a dict
outgoing_invoice_request_dict = outgoing_invoice_request_instance.to_dict()
# create an instance of OutgoingInvoiceRequest from a dict
outgoing_invoice_request_from_dict = OutgoingInvoiceRequest.from_dict(outgoing_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


