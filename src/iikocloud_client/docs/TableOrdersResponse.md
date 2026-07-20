# TableOrdersResponse

Wrapping object (external) for return of orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**orders** | [**List[TableOrderInfo]**](TableOrderInfo.md) | Orders. | 

## Example

```python
from iikocloud_client.models.table_orders_response import TableOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersResponse from a JSON string
table_orders_response_instance = TableOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(TableOrdersResponse.to_json())

# convert the object into a dict
table_orders_response_dict = table_orders_response_instance.to_dict()
# create an instance of TableOrdersResponse from a dict
table_orders_response_from_dict = TableOrdersResponse.from_dict(table_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


