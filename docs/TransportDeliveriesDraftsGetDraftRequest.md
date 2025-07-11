# TransportDeliveriesDraftsGetDraftRequest

Request for an order draft by ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID for which the order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_get_draft_request import TransportDeliveriesDraftsGetDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsGetDraftRequest from a JSON string
transport_deliveries_drafts_get_draft_request_instance = TransportDeliveriesDraftsGetDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsGetDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_get_draft_request_dict = transport_deliveries_drafts_get_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsGetDraftRequest from a dict
transport_deliveries_drafts_get_draft_request_from_dict = TransportDeliveriesDraftsGetDraftRequest.from_dict(transport_deliveries_drafts_get_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


