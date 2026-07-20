# SalesDocumentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banquet** | **bool** | Banquet order flag. Default false. Optional | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**default_store** | **str** | Default store identifier (GUID) | [optional] 
**document_id** | **str** | Document identifier (GUID) | 
**expense_account** | **str** | Expense account identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[SalesDocumentCreateItem]**](SalesDocumentCreateItem.md) | List of document items | 
**number** | **str** | Document number | 
**organization_id** | **str** | Organization identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.sales_document_update_request import SalesDocumentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesDocumentUpdateRequest from a JSON string
sales_document_update_request_instance = SalesDocumentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SalesDocumentUpdateRequest.to_json())

# convert the object into a dict
sales_document_update_request_dict = sales_document_update_request_instance.to_dict()
# create an instance of SalesDocumentUpdateRequest from a dict
sales_document_update_request_from_dict = SalesDocumentUpdateRequest.from_dict(sales_document_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


