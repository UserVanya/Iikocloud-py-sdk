# TransportDeliveriesDraftsDeleteDraftRequest

Delivery order draft deletion request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | ID of the order. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_delete_draft_request import TransportDeliveriesDraftsDeleteDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsDeleteDraftRequest from a JSON string
transport_deliveries_drafts_delete_draft_request_instance = TransportDeliveriesDraftsDeleteDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsDeleteDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_delete_draft_request_dict = transport_deliveries_drafts_delete_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsDeleteDraftRequest from a dict
transport_deliveries_drafts_delete_draft_request_from_dict = TransportDeliveriesDraftsDeleteDraftRequest.from_dict(transport_deliveries_drafts_delete_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


