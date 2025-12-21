# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest

Request for change order's delivery point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**new_delivery_point** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryPoint.md) | New address of delivery. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


