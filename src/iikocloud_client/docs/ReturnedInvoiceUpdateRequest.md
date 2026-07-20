# ReturnedInvoiceUpdateRequest


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
**incoming_invoice_id** | **str** | Associated incoming invoice identifier (GUID) | [optional] 
**items** | [**List[ReturnedInvoiceCreateItem]**](ReturnedInvoiceCreateItem.md) | List of document items | 
**number** | **str** | Document number | 
**organization_id** | **str** | Organization identifier (GUID) | 

## Example

```python
from iikocloud_client.models.returned_invoice_update_request import ReturnedInvoiceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceUpdateRequest from a JSON string
returned_invoice_update_request_instance = ReturnedInvoiceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceUpdateRequest.to_json())

# convert the object into a dict
returned_invoice_update_request_dict = returned_invoice_update_request_instance.to_dict()
# create an instance of ReturnedInvoiceUpdateRequest from a dict
returned_invoice_update_request_from_dict = ReturnedInvoiceUpdateRequest.from_dict(returned_invoice_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


