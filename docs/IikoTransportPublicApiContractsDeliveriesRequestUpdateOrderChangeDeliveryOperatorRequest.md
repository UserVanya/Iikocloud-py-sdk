# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest

Request for assign/change the order operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**operator_id** | **UUID** | Operator to assign the order to. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


