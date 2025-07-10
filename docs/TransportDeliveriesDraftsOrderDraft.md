# TransportDeliveriesDraftsOrderDraft

Order draft object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**locked_by_user** | **str** | ID of the employee, who is editing this draft. | [optional] 
**order** | [**TransportDeliveriesDraftsDeliveryOrderDraft**](TransportDeliveriesDraftsDeliveryOrderDraft.md) | Order. | 
**terminal_group_id** | **str** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_drafts_order_draft import TransportDeliveriesDraftsOrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsOrderDraft from a JSON string
transport_deliveries_drafts_order_draft_instance = TransportDeliveriesDraftsOrderDraft.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsOrderDraft.to_json())

# convert the object into a dict
transport_deliveries_drafts_order_draft_dict = transport_deliveries_drafts_order_draft_instance.to_dict()
# create an instance of TransportDeliveriesDraftsOrderDraft from a dict
transport_deliveries_drafts_order_draft_from_dict = TransportDeliveriesDraftsOrderDraft.from_dict(transport_deliveries_drafts_order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


