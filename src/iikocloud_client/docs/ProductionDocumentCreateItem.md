# ProductionDocumentCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 
**product_size** | **str** | Product size identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.production_document_create_item import ProductionDocumentCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionDocumentCreateItem from a JSON string
production_document_create_item_instance = ProductionDocumentCreateItem.from_json(json)
# print the JSON string representation of the object
print(ProductionDocumentCreateItem.to_json())

# convert the object into a dict
production_document_create_item_dict = production_document_create_item_instance.to_dict()
# create an instance of ProductionDocumentCreateItem from a dict
production_document_create_item_from_dict = ProductionDocumentCreateItem.from_dict(production_document_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


