# ListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Period start date (YYYY-MM-DD format) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**return_full_details** | **bool** | Return full document details: when true, document items and the document revision are added to every list element. Defaults to false — only document headers are returned | [optional] 
**revision** | **int** | Revision for incremental synchronization: only documents with a revision strictly greater than the given value are returned (revision &gt; value). Accepts both a number and a numeric string. Omit to return all documents of the period. Revision is available only in the full document, so when this parameter is set the method additionally requests the documents; if a document revision is unavailable, the document is not returned. The revision of every document is returned in the revision field | [optional] 
**store_ids** | **List[UUID]** | Store identifiers (GUID) to filter the list: only documents having at least one of the given stores (storeFrom/storeTo) are returned. An empty set or an omitted field means no store filtering | [optional] 
**to** | **str** | Period end date (YYYY-MM-DD format) | 

## Example

```python
from iikocloud_client.models.list_request import ListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListRequest from a JSON string
list_request_instance = ListRequest.from_json(json)
# print the JSON string representation of the object
print(ListRequest.to_json())

# convert the object into a dict
list_request_dict = list_request_instance.to_dict()
# create an instance of ListRequest from a dict
list_request_from_dict = ListRequest.from_dict(list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


