# IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse

Wrapping object (external) for a delivery order draft creation/update return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_id** | **UUID** | Order draft order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response import IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response_instance = IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response_dict = iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse from a dict
iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsCreateOrSaveDraftResponse.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_create_or_save_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


