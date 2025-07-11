# TransportTableOrdersResponseTableOrdersResponse

Wrapping object (external) for return of orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**orders** | [**List[TransportTableOrdersResponseTableOrderInfo]**](TransportTableOrdersResponseTableOrderInfo.md) | Orders. | 

## Example

```python
from iikocloud_client.models.transport_table_orders_response_table_orders_response import TransportTableOrdersResponseTableOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersResponseTableOrdersResponse from a JSON string
transport_table_orders_response_table_orders_response_instance = TransportTableOrdersResponseTableOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersResponseTableOrdersResponse.to_json())

# convert the object into a dict
transport_table_orders_response_table_orders_response_dict = transport_table_orders_response_table_orders_response_instance.to_dict()
# create an instance of TransportTableOrdersResponseTableOrdersResponse from a dict
transport_table_orders_response_table_orders_response_from_dict = TransportTableOrdersResponseTableOrdersResponse.from_dict(transport_table_orders_response_table_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


