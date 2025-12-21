# DeliveriesResponseOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_info** | [**DeliveriesResponseOrderOrderInfo**](DeliveriesResponseOrderOrderInfo.md) | Delivery order. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_response import DeliveriesResponseOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderResponse from a JSON string
deliveries_response_order_response_instance = DeliveriesResponseOrderResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderResponse.to_json())

# convert the object into a dict
deliveries_response_order_response_dict = deliveries_response_order_response_instance.to_dict()
# create an instance of DeliveriesResponseOrderResponse from a dict
deliveries_response_order_response_from_dict = DeliveriesResponseOrderResponse.from_dict(deliveries_response_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


