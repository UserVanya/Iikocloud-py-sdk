# TransportDeliveriesResponseOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_info** | [**TransportDeliveriesResponseOrderOrderInfo**](TransportDeliveriesResponseOrderOrderInfo.md) | Delivery order. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_response import TransportDeliveriesResponseOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderResponse from a JSON string
transport_deliveries_response_order_response_instance = TransportDeliveriesResponseOrderResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderResponse.to_json())

# convert the object into a dict
transport_deliveries_response_order_response_dict = transport_deliveries_response_order_response_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderResponse from a dict
transport_deliveries_response_order_response_from_dict = TransportDeliveriesResponseOrderResponse.from_dict(transport_deliveries_response_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


