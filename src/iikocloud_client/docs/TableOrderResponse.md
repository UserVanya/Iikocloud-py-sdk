# TableOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_info** | [**TableOrderInfo**](TableOrderInfo.md) | Order. | 

## Example

```python
from iikocloud_client.models.table_order_response import TableOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderResponse from a JSON string
table_order_response_instance = TableOrderResponse.from_json(json)
# print the JSON string representation of the object
print(TableOrderResponse.to_json())

# convert the object into a dict
table_order_response_dict = table_order_response_instance.to_dict()
# create an instance of TableOrderResponse from a dict
table_order_response_from_dict = TableOrderResponse.from_dict(table_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


