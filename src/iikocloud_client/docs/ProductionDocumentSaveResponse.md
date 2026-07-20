# ProductionDocumentSaveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | [optional] 
**document_number** | **str** | Document number | [optional] 
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.production_document_save_response import ProductionDocumentSaveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionDocumentSaveResponse from a JSON string
production_document_save_response_instance = ProductionDocumentSaveResponse.from_json(json)
# print the JSON string representation of the object
print(ProductionDocumentSaveResponse.to_json())

# convert the object into a dict
production_document_save_response_dict = production_document_save_response_instance.to_dict()
# create an instance of ProductionDocumentSaveResponse from a dict
production_document_save_response_from_dict = ProductionDocumentSaveResponse.from_dict(production_document_save_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


