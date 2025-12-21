# DeliveriesRequestCreateOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.    Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | [optional] 
**create_order_settings** | [**OrdersCommonCreateOrderSettings**](OrdersCommonCreateOrderSettings.md) | Order creation parameters. | [optional] 
**order** | [**DeliveriesRequestCreateOrderDeliveryOrder**](DeliveriesRequestCreateOrderDeliveryOrder.md) | Order. | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_request import DeliveriesRequestCreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderRequest from a JSON string
deliveries_request_create_order_request_instance = DeliveriesRequestCreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderRequest.to_json())

# convert the object into a dict
deliveries_request_create_order_request_dict = deliveries_request_create_order_request_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderRequest from a dict
deliveries_request_create_order_request_from_dict = DeliveriesRequestCreateOrderRequest.from_dict(deliveries_request_create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


