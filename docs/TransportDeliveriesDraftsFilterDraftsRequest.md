# TransportDeliveriesDraftsFilterDraftsRequest

Request for the list of order drafts by several filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organization ID for which the order drafts search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**date_from** | **str** | Draft creation time (UTC). Lower limit. | [optional] 
**date_to** | **str** | Draft creation time (UTC). Upper limit. | [optional] 
**phone** | **str** | Phone number. | [optional] 
**limit** | **int** | Desirable size of result set (50 by default). | [optional] 
**offset** | **int** | Offset from the beginning of full result set for paging. | [optional] 
**source_keys** | **List[str]** | Delivery sources (DeliveryClub, PH and etc.) | [optional] 
**terminal_group_ids** | **List[str]** | List of terminal groups IDs. | [optional] 
**search_text** | **str** | Value for search. Used for prefix search. | [optional] 
**sort_property** | [**TransportDeliveriesDraftsOrderDraftSortProperty**](TransportDeliveriesDraftsOrderDraftSortProperty.md) | Sorting property. | [optional] 
**sort_direction** | [**TransportCommonSortDirection**](TransportCommonSortDirection.md) | Sorting direction. | [optional] 
**operator_ids** | **List[str]** | List of drafts operator IDs. | [optional] 
**order_type_ids** | **List[str]** | List of drafts order type IDs. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_drafts_filter_drafts_request import TransportDeliveriesDraftsFilterDraftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesDraftsFilterDraftsRequest from a JSON string
transport_deliveries_drafts_filter_drafts_request_instance = TransportDeliveriesDraftsFilterDraftsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesDraftsFilterDraftsRequest.to_json())

# convert the object into a dict
transport_deliveries_drafts_filter_drafts_request_dict = transport_deliveries_drafts_filter_drafts_request_instance.to_dict()
# create an instance of TransportDeliveriesDraftsFilterDraftsRequest from a dict
transport_deliveries_drafts_filter_drafts_request_from_dict = TransportDeliveriesDraftsFilterDraftsRequest.from_dict(transport_deliveries_drafts_filter_drafts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


