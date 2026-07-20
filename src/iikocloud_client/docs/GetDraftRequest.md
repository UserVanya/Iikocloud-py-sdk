# GetDraftRequest

Request for an order draft by ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID for which the order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_draft_request import GetDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDraftRequest from a JSON string
get_draft_request_instance = GetDraftRequest.from_json(json)
# print the JSON string representation of the object
print(GetDraftRequest.to_json())

# convert the object into a dict
get_draft_request_dict = get_draft_request_instance.to_dict()
# create an instance of GetDraftRequest from a dict
get_draft_request_from_dict = GetDraftRequest.from_dict(get_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


