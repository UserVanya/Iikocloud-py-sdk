# IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest

Request for a list of edited orders starting from specified revision number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_revision** | **int** | Revision start number beginning from which (but not including) new/edited orders will be returned.                &gt; Maximum revision offset to request - &#x60;3 hours&#x60;. | 
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request_instance = IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request_dict = iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestOrdersByRevisionRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_orders_by_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


