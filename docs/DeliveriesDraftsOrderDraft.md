# DeliveriesDraftsOrderDraft

Order draft object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**locked_by_user** | **UUID** | ID of the employee, who is editing this draft. | [optional] 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**order** | [**DeliveriesDraftsDeliveryOrderDraft**](DeliveriesDraftsDeliveryOrderDraft.md) | Order. | 
**terminal_group_id** | **UUID** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_order_draft import DeliveriesDraftsOrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsOrderDraft from a JSON string
deliveries_drafts_order_draft_instance = DeliveriesDraftsOrderDraft.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsOrderDraft.to_json())

# convert the object into a dict
deliveries_drafts_order_draft_dict = deliveries_drafts_order_draft_instance.to_dict()
# create an instance of DeliveriesDraftsOrderDraft from a dict
deliveries_drafts_order_draft_from_dict = DeliveriesDraftsOrderDraft.from_dict(deliveries_drafts_order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


