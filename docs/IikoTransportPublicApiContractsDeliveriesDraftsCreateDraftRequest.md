# IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest

Draft creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order** | [**IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft**](IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft.md) | Order item. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsCreateDraftRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_create_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


