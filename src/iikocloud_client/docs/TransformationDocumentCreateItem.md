# TransformationDocumentCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.transformation_document_create_item import TransformationDocumentCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransformationDocumentCreateItem from a JSON string
transformation_document_create_item_instance = TransformationDocumentCreateItem.from_json(json)
# print the JSON string representation of the object
print(TransformationDocumentCreateItem.to_json())

# convert the object into a dict
transformation_document_create_item_dict = transformation_document_create_item_instance.to_dict()
# create an instance of TransformationDocumentCreateItem from a dict
transformation_document_create_item_from_dict = TransformationDocumentCreateItem.from_dict(transformation_document_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


