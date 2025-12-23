# DeliveriesDraftsFilterDraftsResponse

Wrapping object (external) for a delivery order drafts return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**drafts** | [**List[DeliveriesDraftsOrderDraft]**](DeliveriesDraftsOrderDraft.md) | Order drafts list. | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_filter_drafts_response import DeliveriesDraftsFilterDraftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsFilterDraftsResponse from a JSON string
deliveries_drafts_filter_drafts_response_instance = DeliveriesDraftsFilterDraftsResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsFilterDraftsResponse.to_json())

# convert the object into a dict
deliveries_drafts_filter_drafts_response_dict = deliveries_drafts_filter_drafts_response_instance.to_dict()
# create an instance of DeliveriesDraftsFilterDraftsResponse from a dict
deliveries_drafts_filter_drafts_response_from_dict = DeliveriesDraftsFilterDraftsResponse.from_dict(deliveries_drafts_filter_drafts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


