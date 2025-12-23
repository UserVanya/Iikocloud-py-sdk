# DeliveriesDraftsGetDraftResponse

Wrapping object (external) for an order draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order** | [**DeliveriesDraftsDeliveryOrderDraft**](DeliveriesDraftsDeliveryOrderDraft.md) | Order draft object. | 
**locked_by_user** | **str** | ID of the employee who is currently editing this draft. | [optional] 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**organization_id** | **str** | Organization ID. | 
**terminal_group_id** | **str** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_get_draft_response import DeliveriesDraftsGetDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsGetDraftResponse from a JSON string
deliveries_drafts_get_draft_response_instance = DeliveriesDraftsGetDraftResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsGetDraftResponse.to_json())

# convert the object into a dict
deliveries_drafts_get_draft_response_dict = deliveries_drafts_get_draft_response_instance.to_dict()
# create an instance of DeliveriesDraftsGetDraftResponse from a dict
deliveries_drafts_get_draft_response_from_dict = DeliveriesDraftsGetDraftResponse.from_dict(deliveries_drafts_get_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


