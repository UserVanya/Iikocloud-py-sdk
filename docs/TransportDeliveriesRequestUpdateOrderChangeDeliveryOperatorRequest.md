# TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest

Request for assign/change the order operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**operator_id** | **str** | Operator to assign the order to. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_change_delivery_operator_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest from a JSON string
transport_deliveries_request_update_order_change_delivery_operator_request_instance = TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_delivery_operator_request_dict = transport_deliveries_request_update_order_change_delivery_operator_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest from a dict
transport_deliveries_request_update_order_change_delivery_operator_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.from_dict(transport_deliveries_request_update_order_change_delivery_operator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


