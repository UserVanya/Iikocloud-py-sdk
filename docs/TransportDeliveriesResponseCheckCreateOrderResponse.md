# TransportDeliveriesResponseCheckCreateOrderResponse

Wrapping object (external) for a delivery check create order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**error_info** | [**TransportErrorsErrorInfo**](TransportErrorsErrorInfo.md) | Order check creation error details. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_check_create_order_response import TransportDeliveriesResponseCheckCreateOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseCheckCreateOrderResponse from a JSON string
transport_deliveries_response_check_create_order_response_instance = TransportDeliveriesResponseCheckCreateOrderResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseCheckCreateOrderResponse.to_json())

# convert the object into a dict
transport_deliveries_response_check_create_order_response_dict = transport_deliveries_response_check_create_order_response_instance.to_dict()
# create an instance of TransportDeliveriesResponseCheckCreateOrderResponse from a dict
transport_deliveries_response_check_create_order_response_from_dict = TransportDeliveriesResponseCheckCreateOrderResponse.from_dict(transport_deliveries_response_check_create_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


