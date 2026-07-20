# IncomingReturnedInvoiceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**default_store** | **str** | Default store identifier (GUID) | [optional] 
**document_id** | **str** | Document identifier (GUID) | 
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[IncomingReturnedInvoiceCreateItem]**](IncomingReturnedInvoiceCreateItem.md) | List of document items | 
**number** | **str** | Document number | 
**organization_id** | **str** | Organization identifier (GUID) | 
**outgoing_invoice_id** | **str** | Associated outgoing invoice identifier (GUID) | [optional] 
**processing_mode** | **str** | Processing mode (RETURN_DISH — return dish, RETURN_GOOD — return ingredients, DO_NOT_RETURN — no warehouse) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_returned_invoice_update_request import IncomingReturnedInvoiceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingReturnedInvoiceUpdateRequest from a JSON string
incoming_returned_invoice_update_request_instance = IncomingReturnedInvoiceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(IncomingReturnedInvoiceUpdateRequest.to_json())

# convert the object into a dict
incoming_returned_invoice_update_request_dict = incoming_returned_invoice_update_request_instance.to_dict()
# create an instance of IncomingReturnedInvoiceUpdateRequest from a dict
incoming_returned_invoice_update_request_from_dict = IncomingReturnedInvoiceUpdateRequest.from_dict(incoming_returned_invoice_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


