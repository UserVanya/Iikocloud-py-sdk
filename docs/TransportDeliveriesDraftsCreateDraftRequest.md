# TransportDeliveriesDraftsCreateDraftRequest

Draft creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order** | [**TransportDeliveriesDraftsDeliveryOrderDraft**](TransportDeliveriesDraftsDeliveryOrderDraft.md) | Order item. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_create_draft_request import TransportDeliveriesDraftsCreateDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsCreateDraftRequest from a JSON string
transport_deliveries_drafts_create_draft_request_instance = TransportDeliveriesDraftsCreateDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsCreateDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_create_draft_request_dict = transport_deliveries_drafts_create_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsCreateDraftRequest from a dict
transport_deliveries_drafts_create_draft_request_from_dict = TransportDeliveriesDraftsCreateDraftRequest.from_dict(transport_deliveries_drafts_create_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


