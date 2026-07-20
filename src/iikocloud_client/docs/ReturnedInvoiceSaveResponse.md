# ReturnedInvoiceSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.returned_invoice_save_response import ReturnedInvoiceSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedInvoiceSaveResponse from a JSON string
returned_invoice_save_response_instance = ReturnedInvoiceSaveResponse.from_json(json)
# print the JSON string representation of the object
print(ReturnedInvoiceSaveResponse.to_json())

# convert the object into a dict
returned_invoice_save_response_dict = returned_invoice_save_response_instance.to_dict()
# create an instance of ReturnedInvoiceSaveResponse from a dict
returned_invoice_save_response_from_dict = ReturnedInvoiceSaveResponse.from_dict(returned_invoice_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


