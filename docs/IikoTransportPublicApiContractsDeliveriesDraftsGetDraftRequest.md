# IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest

Request for an order draft by ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID for which the order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsGetDraftRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_get_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


