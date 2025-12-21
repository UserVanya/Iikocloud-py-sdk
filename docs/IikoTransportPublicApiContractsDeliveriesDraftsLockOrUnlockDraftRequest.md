# IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest

Delivery order draft lock or unlock request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | ID of the order. | 
**employee_id** | **UUID** | ID of the employee. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsLockOrUnlockDraftRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_lock_or_unlock_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


