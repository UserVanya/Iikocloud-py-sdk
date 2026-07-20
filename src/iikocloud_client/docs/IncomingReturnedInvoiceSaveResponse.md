# IncomingReturnedInvoiceSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.incoming_returned_invoice_save_response import IncomingReturnedInvoiceSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingReturnedInvoiceSaveResponse from a JSON string
incoming_returned_invoice_save_response_instance = IncomingReturnedInvoiceSaveResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingReturnedInvoiceSaveResponse.to_json())

# convert the object into a dict
incoming_returned_invoice_save_response_dict = incoming_returned_invoice_save_response_instance.to_dict()
# create an instance of IncomingReturnedInvoiceSaveResponse from a dict
incoming_returned_invoice_save_response_from_dict = IncomingReturnedInvoiceSaveResponse.from_dict(incoming_returned_invoice_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


