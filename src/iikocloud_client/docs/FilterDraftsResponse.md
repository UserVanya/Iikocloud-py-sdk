# FilterDraftsResponse

Wrapping object (external) for a delivery order drafts return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**drafts** | [**List[OrderDraft]**](OrderDraft.md) | Order drafts list. | 

## Example

```python
from iikocloud_client.models.filter_drafts_response import FilterDraftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDraftsResponse from a JSON string
filter_drafts_response_instance = FilterDraftsResponse.from_json(json)
# print the JSON string representation of the object
print(FilterDraftsResponse.to_json())

# convert the object into a dict
filter_drafts_response_dict = filter_drafts_response_instance.to_dict()
# create an instance of FilterDraftsResponse from a dict
filter_drafts_response_from_dict = FilterDraftsResponse.from_dict(filter_drafts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


