# IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date** | **str** | Actual delivery time. If empty local iikoFront time will used.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request import IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request_instance = IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request_dict = iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


