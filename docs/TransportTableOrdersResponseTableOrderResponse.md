# TransportTableOrdersResponseTableOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_info** | [**TransportTableOrdersResponseTableOrderInfo**](TransportTableOrdersResponseTableOrderInfo.md) | Order. | 

## Example

```python
from iikocloud_client.models.transport_table_orders_response_table_order_response import TransportTableOrdersResponseTableOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersResponseTableOrderResponse from a JSON string
transport_table_orders_response_table_order_response_instance = TransportTableOrdersResponseTableOrderResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersResponseTableOrderResponse.to_json())

# convert the object into a dict
transport_table_orders_response_table_order_response_dict = transport_table_orders_response_table_order_response_instance.to_dict()
# create an instance of TransportTableOrdersResponseTableOrderResponse from a dict
transport_table_orders_response_table_order_response_from_dict = TransportTableOrdersResponseTableOrderResponse.from_dict(transport_table_orders_response_table_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


