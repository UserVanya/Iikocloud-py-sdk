# DeliveriesRequestCloseDeliveryOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date** | **str** | Actual delivery time. If empty local iikoFront time will used.   &gt; Allowed from version &#x60;8.0.6&#x60;. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_close_delivery_order_request import DeliveriesRequestCloseDeliveryOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCloseDeliveryOrderRequest from a JSON string
deliveries_request_close_delivery_order_request_instance = DeliveriesRequestCloseDeliveryOrderRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCloseDeliveryOrderRequest.to_json())

# convert the object into a dict
deliveries_request_close_delivery_order_request_dict = deliveries_request_close_delivery_order_request_instance.to_dict()
# create an instance of DeliveriesRequestCloseDeliveryOrderRequest from a dict
deliveries_request_close_delivery_order_request_from_dict = DeliveriesRequestCloseDeliveryOrderRequest.from_dict(deliveries_request_close_delivery_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


