# IikoTransportPublicApiContractsDeliveriesResponseOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_info** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo.md) | Delivery order. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_response import IikoTransportPublicApiContractsDeliveriesResponseOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_response_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_response_dict = iiko_transport_public_api_contracts_deliveries_response_order_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderResponse from a dict
iiko_transport_public_api_contracts_deliveries_response_order_response_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderResponse.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


