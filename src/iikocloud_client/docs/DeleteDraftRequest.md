# DeleteDraftRequest

Delivery order draft deletion request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | ID of the order. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.delete_draft_request import DeleteDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDraftRequest from a JSON string
delete_draft_request_instance = DeleteDraftRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteDraftRequest.to_json())

# convert the object into a dict
delete_draft_request_dict = delete_draft_request_instance.to_dict()
# create an instance of DeleteDraftRequest from a dict
delete_draft_request_from_dict = DeleteDraftRequest.from_dict(delete_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


