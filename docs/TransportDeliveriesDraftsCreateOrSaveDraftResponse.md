# TransportDeliveriesDraftsCreateOrSaveDraftResponse

Wrapping object (external) for a delivery order draft creation/update return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_id** | **str** | Order draft order ID. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_drafts_create_or_save_draft_response import TransportDeliveriesDraftsCreateOrSaveDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsCreateOrSaveDraftResponse from a JSON string
transport_deliveries_drafts_create_or_save_draft_response_instance = TransportDeliveriesDraftsCreateOrSaveDraftResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsCreateOrSaveDraftResponse.to_json())

# convert the object into a dict
transport_deliveries_drafts_create_or_save_draft_response_dict = transport_deliveries_drafts_create_or_save_draft_response_instance.to_dict()
# create an instance of TransportDeliveriesDraftsCreateOrSaveDraftResponse from a dict
transport_deliveries_drafts_create_or_save_draft_response_from_dict = TransportDeliveriesDraftsCreateOrSaveDraftResponse.from_dict(transport_deliveries_drafts_create_or_save_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


