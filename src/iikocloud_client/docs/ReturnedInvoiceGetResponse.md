# ReturnedInvoiceGetResponse


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
**incoming_invoice_id** | **str** | Associated incoming invoice identifier (GUID) | [optional] 
**items** | [**List[ReturnedInvoiceGetItem]**](ReturnedInvoiceGetItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.returned_invoice_get_response import ReturnedInvoiceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceGetResponse from a JSON string
returned_invoice_get_response_instance = ReturnedInvoiceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceGetResponse.to_json())

# convert the object into a dict
returned_invoice_get_response_dict = returned_invoice_get_response_instance.to_dict()
# create an instance of ReturnedInvoiceGetResponse from a dict
returned_invoice_get_response_from_dict = ReturnedInvoiceGetResponse.from_dict(returned_invoice_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


