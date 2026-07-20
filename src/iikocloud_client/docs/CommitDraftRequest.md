# CommitDraftRequest

Delivery order draft commitment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_order_settings** | [**CreateOrderSettings**](CreateOrderSettings.md) | Order creation parameters. | [optional] 
**order_id** | **UUID** | ID of the order. | 
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.commit_draft_request import CommitDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommitDraftRequest from a JSON string
commit_draft_request_instance = CommitDraftRequest.from_json(json)
# print the JSON string representation of the object
print(CommitDraftRequest.to_json())

# convert the object into a dict
commit_draft_request_dict = commit_draft_request_instance.to_dict()
# create an instance of CommitDraftRequest from a dict
commit_draft_request_from_dict = CommitDraftRequest.from_dict(commit_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


