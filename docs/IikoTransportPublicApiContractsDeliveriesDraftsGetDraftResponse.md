# IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse

Wrapping object (external) for an order draft.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order** | [**IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft**](IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft.md) | Order draft object. | 
**locked_by_user** | **UUID** | ID of the employee who is currently editing this draft. | [optional] 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**organization_id** | **UUID** | Organization ID. | 
**terminal_group_id** | **UUID** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response import IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response_instance = IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response_dict = iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse from a dict
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsGetDraftResponse.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_get_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


