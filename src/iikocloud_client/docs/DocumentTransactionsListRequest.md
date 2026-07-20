# DocumentTransactionsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 

## Example

```python
from iikocloud_client.models.document_transactions_list_request import DocumentTransactionsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentTransactionsListRequest from a JSON string
document_transactions_list_request_instance = DocumentTransactionsListRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentTransactionsListRequest.to_json())

# convert the object into a dict
document_transactions_list_request_dict = document_transactions_list_request_instance.to_dict()
# create an instance of DocumentTransactionsListRequest from a dict
document_transactions_list_request_from_dict = DocumentTransactionsListRequest.from_dict(document_transactions_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


