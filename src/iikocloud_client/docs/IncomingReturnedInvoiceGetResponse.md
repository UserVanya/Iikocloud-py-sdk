# IncomingReturnedInvoiceGetResponse


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
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[IncomingReturnedInvoiceGetItem]**](IncomingReturnedInvoiceGetItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**outgoing_invoice_id** | **str** | Associated outgoing invoice identifier (GUID) | [optional] 
**processing_mode** | **str** | Processing mode (RETURN_DISH — return dish, RETURN_GOOD — return ingredients, DO_NOT_RETURN — no warehouse) | [optional] 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_returned_invoice_get_response import IncomingReturnedInvoiceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingReturnedInvoiceGetResponse from a JSON string
incoming_returned_invoice_get_response_instance = IncomingReturnedInvoiceGetResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingReturnedInvoiceGetResponse.to_json())

# convert the object into a dict
incoming_returned_invoice_get_response_dict = incoming_returned_invoice_get_response_instance.to_dict()
# create an instance of IncomingReturnedInvoiceGetResponse from a dict
incoming_returned_invoice_get_response_from_dict = IncomingReturnedInvoiceGetResponse.from_dict(incoming_returned_invoice_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


