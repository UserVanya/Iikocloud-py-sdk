# TransportDeliveriesDraftsGetDraftResponse

Wrapping object (external) for an order draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order** | [**TransportDeliveriesDraftsDeliveryOrderDraft**](TransportDeliveriesDraftsDeliveryOrderDraft.md) | Order draft object. | 
**locked_by_user** | **str** | ID of the employee who is currently editing this draft. | 
**organization_id** | **str** | Organization ID. | 
**terminal_group_id** | **str** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_get_draft_response import TransportDeliveriesDraftsGetDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsGetDraftResponse from a JSON string
transport_deliveries_drafts_get_draft_response_instance = TransportDeliveriesDraftsGetDraftResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsGetDraftResponse.to_json())

# convert the object into a dict
transport_deliveries_drafts_get_draft_response_dict = transport_deliveries_drafts_get_draft_response_instance.to_dict()
# create an instance of TransportDeliveriesDraftsGetDraftResponse from a dict
transport_deliveries_drafts_get_draft_response_from_dict = TransportDeliveriesDraftsGetDraftResponse.from_dict(transport_deliveries_drafts_get_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


