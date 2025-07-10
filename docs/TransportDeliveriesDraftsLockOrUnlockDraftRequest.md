# TransportDeliveriesDraftsLockOrUnlockDraftRequest

Delivery order draft lock or unlock request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | ID of the order. | 
**employee_id** | **str** | ID of the employee. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_drafts_lock_or_unlock_draft_request import TransportDeliveriesDraftsLockOrUnlockDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsLockOrUnlockDraftRequest from a JSON string
transport_deliveries_drafts_lock_or_unlock_draft_request_instance = TransportDeliveriesDraftsLockOrUnlockDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsLockOrUnlockDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_lock_or_unlock_draft_request_dict = transport_deliveries_drafts_lock_or_unlock_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsLockOrUnlockDraftRequest from a dict
transport_deliveries_drafts_lock_or_unlock_draft_request_from_dict = TransportDeliveriesDraftsLockOrUnlockDraftRequest.from_dict(transport_deliveries_drafts_lock_or_unlock_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


