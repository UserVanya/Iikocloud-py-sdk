# LockOrUnlockDraftRequest

Delivery order draft lock or unlock request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | ID of the employee. | 
**order_id** | **UUID** | ID of the order. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.lock_or_unlock_draft_request import LockOrUnlockDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockOrUnlockDraftRequest from a JSON string
lock_or_unlock_draft_request_instance = LockOrUnlockDraftRequest.from_json(json)
# print the JSON string representation of the object
print(LockOrUnlockDraftRequest.to_json())

# convert the object into a dict
lock_or_unlock_draft_request_dict = lock_or_unlock_draft_request_instance.to_dict()
# create an instance of LockOrUnlockDraftRequest from a dict
lock_or_unlock_draft_request_from_dict = LockOrUnlockDraftRequest.from_dict(lock_or_unlock_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


