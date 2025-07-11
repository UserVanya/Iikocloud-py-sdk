# TransportDeliveriesRequestCreateOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID the order must be sent to.    Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 
**create_order_settings** | [**TransportOrdersCommonCreateOrderSettings**](TransportOrdersCommonCreateOrderSettings.md) | Order creation parameters. | [optional] 
**order** | [**TransportDeliveriesRequestCreateOrderDeliveryOrder**](TransportDeliveriesRequestCreateOrderDeliveryOrder.md) | Order. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_request import TransportDeliveriesRequestCreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderRequest from a JSON string
transport_deliveries_request_create_order_request_instance = TransportDeliveriesRequestCreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderRequest.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_request_dict = transport_deliveries_request_create_order_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderRequest from a dict
transport_deliveries_request_create_order_request_from_dict = TransportDeliveriesRequestCreateOrderRequest.from_dict(transport_deliveries_request_create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


