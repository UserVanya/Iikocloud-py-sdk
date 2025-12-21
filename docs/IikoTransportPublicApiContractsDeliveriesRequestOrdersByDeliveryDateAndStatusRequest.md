# IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest

Request for information about orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**delivery_date_from** | **str** | Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the &#x60;/deliveries/history/by_delivery_date_and_phone&#x60; method. | 
**delivery_date_to** | **str** | Order delivery date (Local for delivery terminal). Upper limit. | [optional] 
**statuses** | [**List[IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus]**](IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus.md) | Allowed order statuses. | [optional] 
**source_keys** | **List[str]** | Source keys. | [optional] 
**courier_ids** | **List[UUID]** | List of driver IDs. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request import IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request_instance = IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request_dict = iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestOrdersByDeliveryDateAndStatusRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_orders_by_delivery_date_and_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


