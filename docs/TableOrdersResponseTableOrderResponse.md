# TableOrdersResponseTableOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_info** | [**TableOrdersResponseTableOrderInfo**](TableOrdersResponseTableOrderInfo.md) | Order. | 

## Example

```python
from iikocloud_client.models.table_orders_response_table_order_response import TableOrdersResponseTableOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersResponseTableOrderResponse from a JSON string
table_orders_response_table_order_response_instance = TableOrdersResponseTableOrderResponse.from_json(json)
# print the JSON string representation of the object
print(TableOrdersResponseTableOrderResponse.to_json())

# convert the object into a dict
table_orders_response_table_order_response_dict = table_orders_response_table_order_response_instance.to_dict()
# create an instance of TableOrdersResponseTableOrderResponse from a dict
table_orders_response_table_order_response_from_dict = TableOrdersResponseTableOrderResponse.from_dict(table_orders_response_table_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


