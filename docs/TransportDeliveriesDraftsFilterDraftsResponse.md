# TransportDeliveriesDraftsFilterDraftsResponse

Wrapping object (external) for a delivery order drafts return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**drafts** | [**List[TransportDeliveriesDraftsOrderDraft]**](TransportDeliveriesDraftsOrderDraft.md) | Order drafts list. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_drafts_filter_drafts_response import TransportDeliveriesDraftsFilterDraftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsFilterDraftsResponse from a JSON string
transport_deliveries_drafts_filter_drafts_response_instance = TransportDeliveriesDraftsFilterDraftsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsFilterDraftsResponse.to_json())

# convert the object into a dict
transport_deliveries_drafts_filter_drafts_response_dict = transport_deliveries_drafts_filter_drafts_response_instance.to_dict()
# create an instance of TransportDeliveriesDraftsFilterDraftsResponse from a dict
transport_deliveries_drafts_filter_drafts_response_from_dict = TransportDeliveriesDraftsFilterDraftsResponse.from_dict(transport_deliveries_drafts_filter_drafts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


