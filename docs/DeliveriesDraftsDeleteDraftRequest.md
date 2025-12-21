# DeliveriesDraftsDeleteDraftRequest

Delivery order draft deletion request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | ID of the order. | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_delete_draft_request import DeliveriesDraftsDeleteDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsDeleteDraftRequest from a JSON string
deliveries_drafts_delete_draft_request_instance = DeliveriesDraftsDeleteDraftRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsDeleteDraftRequest.to_json())

# convert the object into a dict
deliveries_drafts_delete_draft_request_dict = deliveries_drafts_delete_draft_request_instance.to_dict()
# create an instance of DeliveriesDraftsDeleteDraftRequest from a dict
deliveries_drafts_delete_draft_request_from_dict = DeliveriesDraftsDeleteDraftRequest.from_dict(deliveries_drafts_delete_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


