# DeliveriesDraftsSaveDraftRequest

Draft editing model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | ID of the employee who wants to update order draft. | 
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order** | [**DeliveriesDraftsDeliveryOrderDraft**](DeliveriesDraftsDeliveryOrderDraft.md) | Order item. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_drafts_save_draft_request import DeliveriesDraftsSaveDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesDraftsSaveDraftRequest from a JSON string
deliveries_drafts_save_draft_request_instance = DeliveriesDraftsSaveDraftRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesDraftsSaveDraftRequest.to_json())

# convert the object into a dict
deliveries_drafts_save_draft_request_dict = deliveries_drafts_save_draft_request_instance.to_dict()
# create an instance of DeliveriesDraftsSaveDraftRequest from a dict
deliveries_drafts_save_draft_request_from_dict = DeliveriesDraftsSaveDraftRequest.from_dict(deliveries_drafts_save_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


