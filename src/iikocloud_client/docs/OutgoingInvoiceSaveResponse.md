# OutgoingInvoiceSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_invoice_save_response import OutgoingInvoiceSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingInvoiceSaveResponse from a JSON string
outgoing_invoice_save_response_instance = OutgoingInvoiceSaveResponse.from_json(json)
# print the JSON string representation of the object
print(OutgoingInvoiceSaveResponse.to_json())

# convert the object into a dict
outgoing_invoice_save_response_dict = outgoing_invoice_save_response_instance.to_dict()
# create an instance of OutgoingInvoiceSaveResponse from a dict
outgoing_invoice_save_response_from_dict = OutgoingInvoiceSaveResponse.from_dict(outgoing_invoice_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


