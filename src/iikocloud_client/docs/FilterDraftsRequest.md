# FilterDraftsRequest

Request for the list of order drafts by several filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Draft creation time (UTC). Lower limit. | [optional] 
**date_to** | **str** | Draft creation time (UTC). Upper limit. | [optional] 
**limit** | **int** | Desirable size of result set (50 by default). | [optional] 
**offset** | **int** | Offset from the beginning of full result set for paging. | [optional] 
**operator_ids** | **List[UUID]** | List of drafts operator IDs. | [optional] 
**order_type_ids** | **List[UUID]** | List of drafts order type IDs. | [optional] 
**organization_ids** | **List[UUID]** | Organization ID for which the order drafts search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**phone** | **str** | Phone number. | [optional] 
**search_text** | **str** | Value for search. Used for prefix search. | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) | Sorting direction. | [optional] 
**sort_property** | [**OrderDraftSortProperty**](OrderDraftSortProperty.md) | Sorting property. | [optional] 
**source_keys** | **List[str]** | Delivery sources (DeliveryClub, PH and etc.) | [optional] 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs. | [optional] 

## Example

```python
from iikocloud_client.models.filter_drafts_request import FilterDraftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDraftsRequest from a JSON string
filter_drafts_request_instance = FilterDraftsRequest.from_json(json)
# print the JSON string representation of the object
print(FilterDraftsRequest.to_json())

# convert the object into a dict
filter_drafts_request_dict = filter_drafts_request_instance.to_dict()
# create an instance of FilterDraftsRequest from a dict
filter_drafts_request_from_dict = FilterDraftsRequest.from_dict(filter_drafts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


