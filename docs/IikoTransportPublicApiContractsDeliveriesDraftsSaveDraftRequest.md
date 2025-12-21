# IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest

Draft editing model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | ID of the employee who wants to update order draft. | 
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order** | [**IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft**](IikoTransportPublicApiContractsDeliveriesDraftsDeliveryOrderDraft.md) | Order item. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request import IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request_instance = IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request_dict = iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest from a dict
iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsSaveDraftRequest.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_save_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


