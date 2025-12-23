# DeliveriesDraftsCreateOrSaveDraftResponse

Wrapping object (external) for a delivery order draft creation/update return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_id** | **str** | Order draft order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_drafts_create_or_save_draft_response import DeliveriesDraftsCreateOrSaveDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsCreateOrSaveDraftResponse from a JSON string
deliveries_drafts_create_or_save_draft_response_instance = DeliveriesDraftsCreateOrSaveDraftResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsCreateOrSaveDraftResponse.to_json())

# convert the object into a dict
deliveries_drafts_create_or_save_draft_response_dict = deliveries_drafts_create_or_save_draft_response_instance.to_dict()
# create an instance of DeliveriesDraftsCreateOrSaveDraftResponse from a dict
deliveries_drafts_create_or_save_draft_response_from_dict = DeliveriesDraftsCreateOrSaveDraftResponse.from_dict(deliveries_drafts_create_or_save_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


