# DeliveriesDraftsLockOrUnlockDraftRequest

Delivery order draft lock or unlock request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | ID of the order. | 
**employee_id** | **str** | ID of the employee. | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_lock_or_unlock_draft_request import DeliveriesDraftsLockOrUnlockDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsLockOrUnlockDraftRequest from a JSON string
deliveries_drafts_lock_or_unlock_draft_request_instance = DeliveriesDraftsLockOrUnlockDraftRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsLockOrUnlockDraftRequest.to_json())

# convert the object into a dict
deliveries_drafts_lock_or_unlock_draft_request_dict = deliveries_drafts_lock_or_unlock_draft_request_instance.to_dict()
# create an instance of DeliveriesDraftsLockOrUnlockDraftRequest from a dict
deliveries_drafts_lock_or_unlock_draft_request_from_dict = DeliveriesDraftsLockOrUnlockDraftRequest.from_dict(deliveries_drafts_lock_or_unlock_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


