# GetDraftResponse

Wrapping object (external) for an order draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**created_at** | **str** | Draft creation time (UTC). | 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**locked_by_user** | **UUID** | ID of the employee who is currently editing this draft. | [optional] 
**order** | [**DeliveryOrderDraft**](DeliveryOrderDraft.md) | Order draft object. | 
**organization_id** | **UUID** | Organization ID. | 
**terminal_group_id** | **UUID** | Terminal group ID. | [optional] 

## Example

```python
from iikocloud_client.models.get_draft_response import GetDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDraftResponse from a JSON string
get_draft_response_instance = GetDraftResponse.from_json(json)
# print the JSON string representation of the object
print(GetDraftResponse.to_json())

# convert the object into a dict
get_draft_response_dict = get_draft_response_instance.to_dict()
# create an instance of GetDraftResponse from a dict
get_draft_response_from_dict = GetDraftResponse.from_dict(get_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


