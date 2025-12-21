# IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest

Request for the list of order drafts by several filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization ID for which the order drafts search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**date_from** | **str** | Draft creation time (UTC). Lower limit. | [optional] 
**date_to** | **str** | Draft creation time (UTC). Upper limit. | [optional] 
**phone** | **str** | Phone number. | [optional] 
**limit** | **int** | Desirable size of result set (50 by default). | [optional] 
**offset** | **int** | Offset from the beginning of full result set for paging. | [optional] 
**source_keys** | **List[str]** | Delivery sources (DeliveryClub, PH and etc.) | [optional] 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs. | [optional] 
**search_text** | **str** | Value for search. Used for prefix search. | [optional] 
**sort_property** | [**IikoTransportPublicApiContractsDeliveriesDraftsOrderDraftSortProperty**](IikoTransportPublicApiContractsDeliveriesDraftsOrderDraftSortProperty.md) | Sorting property. | [optional] 
**sort_direction** | [**IikoTransportPublicApiContractsCommonSortDirection**](IikoTransportPublicApiContractsCommonSortDirection.md) | Sorting direction. | [optional] 
**operator_ids** | **List[UUID]** | List of drafts operator IDs. | [optional] 
**order_type_ids** | **List[UUID]** | List of drafts order type IDs. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request import IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


