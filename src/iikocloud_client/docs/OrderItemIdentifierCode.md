# OrderItemIdentifierCode

OrderItem's IdentifierCode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**IdentifierCode**](IdentifierCode.md) | Product code. | 
**flags** | **List[str]** | Application flags. | 
**id** | **UUID** | Id of order&#39;s position. | 

## Example

```python
from iikocloud_client.models.order_item_identifier_code import OrderItemIdentifierCode

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemIdentifierCode from a JSON string
order_item_identifier_code_instance = OrderItemIdentifierCode.from_json(json)
# print the JSON string representation of the object
print(OrderItemIdentifierCode.to_json())

# convert the object into a dict
order_item_identifier_code_dict = order_item_identifier_code_instance.to_dict()
# create an instance of OrderItemIdentifierCode from a dict
order_item_identifier_code_from_dict = OrderItemIdentifierCode.from_dict(order_item_identifier_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


