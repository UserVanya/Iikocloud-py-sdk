# TransportDeliveriesDraftsCommitDraftRequest

Delivery order draft commitment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 
**create_order_settings** | [**TransportOrdersCommonCreateOrderSettings**](TransportOrdersCommonCreateOrderSettings.md) | Order creation parameters. | [optional] 
**order_id** | **str** | ID of the order. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_drafts_commit_draft_request import TransportDeliveriesDraftsCommitDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsCommitDraftRequest from a JSON string
transport_deliveries_drafts_commit_draft_request_instance = TransportDeliveriesDraftsCommitDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsCommitDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_commit_draft_request_dict = transport_deliveries_drafts_commit_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsCommitDraftRequest from a dict
transport_deliveries_drafts_commit_draft_request_from_dict = TransportDeliveriesDraftsCommitDraftRequest.from_dict(transport_deliveries_drafts_commit_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


