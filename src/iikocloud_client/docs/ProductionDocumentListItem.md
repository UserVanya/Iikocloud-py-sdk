# ProductionDocumentListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**deleted** | **bool** | Flag indicating that the document is deleted | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**number** | **str** | Document number | [optional] 
**processed** | **bool** | Flag indicating that the document is processed | [optional] 
**store_from** | **str** | Write-off store identifier (GUID) | [optional] 
**store_to** | **str** | Receipt store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.production_document_list_item import ProductionDocumentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductionDocumentListItem from a JSON string
production_document_list_item_instance = ProductionDocumentListItem.from_json(json)
# print the JSON string representation of the object
print(ProductionDocumentListItem.to_json())

# convert the object into a dict
production_document_list_item_dict = production_document_list_item_instance.to_dict()
# create an instance of ProductionDocumentListItem from a dict
production_document_list_item_from_dict = ProductionDocumentListItem.from_dict(production_document_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


