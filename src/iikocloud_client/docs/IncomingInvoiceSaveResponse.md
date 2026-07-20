# IncomingInvoiceSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.incoming_invoice_save_response import IncomingInvoiceSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoiceSaveResponse from a JSON string
incoming_invoice_save_response_instance = IncomingInvoiceSaveResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoiceSaveResponse.to_json())

# convert the object into a dict
incoming_invoice_save_response_dict = incoming_invoice_save_response_instance.to_dict()
# create an instance of IncomingInvoiceSaveResponse from a dict
incoming_invoice_save_response_from_dict = IncomingInvoiceSaveResponse.from_dict(incoming_invoice_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


