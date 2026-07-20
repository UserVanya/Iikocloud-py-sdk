# SalesDocumentSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.sales_document_save_response import SalesDocumentSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalesDocumentSaveResponse from a JSON string
sales_document_save_response_instance = SalesDocumentSaveResponse.from_json(json)
# print the JSON string representation of the object
print(SalesDocumentSaveResponse.to_json())

# convert the object into a dict
sales_document_save_response_dict = sales_document_save_response_instance.to_dict()
# create an instance of SalesDocumentSaveResponse from a dict
sales_document_save_response_from_dict = SalesDocumentSaveResponse.from_dict(sales_document_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


