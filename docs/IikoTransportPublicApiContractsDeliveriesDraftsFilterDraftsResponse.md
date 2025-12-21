# IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse

Wrapping object (external) for a delivery order drafts return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**drafts** | [**List[IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft]**](IikoTransportPublicApiContractsDeliveriesDraftsOrderDraft.md) | Order drafts list. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response import IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response_instance = IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response_dict = iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse from a dict
iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response_from_dict = IikoTransportPublicApiContractsDeliveriesDraftsFilterDraftsResponse.from_dict(iiko_transport_public_api_contracts_deliveries_drafts_filter_drafts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


