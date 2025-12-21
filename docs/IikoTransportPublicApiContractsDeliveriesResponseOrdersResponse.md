# IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**orders** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo.md) | Orders. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_response_orders_response_instance = IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_orders_response_dict = iiko_transport_public_api_contracts_deliveries_response_orders_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse from a dict
iiko_transport_public_api_contracts_deliveries_response_orders_response_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrdersResponse.from_dict(iiko_transport_public_api_contracts_deliveries_response_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


