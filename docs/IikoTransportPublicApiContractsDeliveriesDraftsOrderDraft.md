# IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft

Order draft object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**locked_by_user** | **UUID** | ID of the employee, who is editing this draft. | [optional] 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**order** | [**IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft**](IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft.md) | Order. | 
**terminal_group_id** | **UUID** | Terminal group ID. | [optional] 
**created_at** | **str** | Draft creation time (UTC). | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_order_draft import IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_order_draft_instance = IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_order_draft_dict = iiko_transport_public_api_contracts_deliveries_drafts_order_draft_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft from a dict
iiko_transport_public_api_contracts_deliveries_drafts_order_draft_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


