# SaveDraftRequest

Draft editing model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | ID of the employee who wants to update order draft. | 
**order** | [**DeliveryOrderDraft**](DeliveryOrderDraft.md) | Order item. | 
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.save_draft_request import SaveDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveDraftRequest from a JSON string
save_draft_request_instance = SaveDraftRequest.from_json(json)
# print the JSON string representation of the object
print(SaveDraftRequest.to_json())

# convert the object into a dict
save_draft_request_dict = save_draft_request_instance.to_dict()
# create an instance of SaveDraftRequest from a dict
save_draft_request_from_dict = SaveDraftRequest.from_dict(save_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


