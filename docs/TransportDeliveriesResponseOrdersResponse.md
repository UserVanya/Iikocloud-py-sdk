# TransportDeliveriesResponseOrdersResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**orders** | [**List[TransportDeliveriesResponseOrderOrderInfo]**](TransportDeliveriesResponseOrderOrderInfo.md) | Orders. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_orders_response import TransportDeliveriesResponseOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrdersResponse from a JSON string
transport_deliveries_response_orders_response_instance = TransportDeliveriesResponseOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrdersResponse.to_json())

# convert the object into a dict
transport_deliveries_response_orders_response_dict = transport_deliveries_response_orders_response_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrdersResponse from a dict
transport_deliveries_response_orders_response_from_dict = TransportDeliveriesResponseOrdersResponse.from_dict(transport_deliveries_response_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


