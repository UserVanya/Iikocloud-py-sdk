# IncomingInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
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
**items** | [**List[IncomingInvoiceRequestItem]**](IncomingInvoiceRequestItem.md) | List of document items | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**transport_invoice_number** | **str** | Transport invoice number | [optional] 

## Example

```python
from iikocloud_client.models.incoming_invoice_request import IncomingInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoiceRequest from a JSON string
incoming_invoice_request_instance = IncomingInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoiceRequest.to_json())

# convert the object into a dict
incoming_invoice_request_dict = incoming_invoice_request_instance.to_dict()
# create an instance of IncomingInvoiceRequest from a dict
incoming_invoice_request_from_dict = IncomingInvoiceRequest.from_dict(incoming_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


