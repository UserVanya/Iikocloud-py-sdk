# IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest

Delivery order draft commitment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 
**create_order_settings** | [**IikoTransportPublicApiContractsOrdersCommonCreateOrderSettings**](IikoTransportPublicApiContractsOrdersCommonCreateOrderSettings.md) | Order creation parameters. | [optional] 
**order_id** | **UUID** | ID of the order. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsCommitDraftRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_commit_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


