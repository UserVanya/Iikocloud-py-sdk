# TransportDeliveriesDraftsSaveDraftRequest

Draft editing model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | ID of the employee who wants to update order draft. | 
**organization_id** | **str** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order** | [**TransportDeliveriesDraftsDeliveryOrderDraft**](TransportDeliveriesDraftsDeliveryOrderDraft.md) | Order item. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_save_draft_request import TransportDeliveriesDraftsSaveDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsSaveDraftRequest from a JSON string
transport_deliveries_drafts_save_draft_request_instance = TransportDeliveriesDraftsSaveDraftRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsSaveDraftRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_save_draft_request_dict = transport_deliveries_drafts_save_draft_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsSaveDraftRequest from a dict
transport_deliveries_drafts_save_draft_request_from_dict = TransportDeliveriesDraftsSaveDraftRequest.from_dict(transport_deliveries_drafts_save_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


