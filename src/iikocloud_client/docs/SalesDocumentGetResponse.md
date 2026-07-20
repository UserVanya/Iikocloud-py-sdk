# SalesDocumentGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banquet** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**conception** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**default_store** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**expense_account** | **str** |  | [optional] 
**is_automatic** | **bool** |  | [optional] 
**is_editable** | **bool** |  | [optional] 
**items** | [**List[SalesDocumentGetItem]**](SalesDocumentGetItem.md) |  | [optional] 
**number** | **str** |  | [optional] 
**revenue_account** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**user_created** | **str** |  | [optional] 
**user_modified** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.sales_document_get_response import SalesDocumentGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalesDocumentGetResponse from a JSON string
sales_document_get_response_instance = SalesDocumentGetResponse.from_json(json)
# print the JSON string representation of the object
print(SalesDocumentGetResponse.to_json())

# convert the object into a dict
sales_document_get_response_dict = sales_document_get_response_instance.to_dict()
# create an instance of SalesDocumentGetResponse from a dict
sales_document_get_response_from_dict = SalesDocumentGetResponse.from_dict(sales_document_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


