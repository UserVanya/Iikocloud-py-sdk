# DeliveriesResponseOrderOrderItemIdentifierCode

OrderItem's IdentifierCode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of order&#39;s position. | 
**code** | [**DeliveriesResponseOrderIdentifierCode**](DeliveriesResponseOrderIdentifierCode.md) | Product code. | 
**flags** | **List[str]** | Application flags. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_order_item_identifier_code import DeliveriesResponseOrderOrderItemIdentifierCode

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderOrderItemIdentifierCode from a JSON string
deliveries_response_order_order_item_identifier_code_instance = DeliveriesResponseOrderOrderItemIdentifierCode.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderOrderItemIdentifierCode.to_json())

# convert the object into a dict
deliveries_response_order_order_item_identifier_code_dict = deliveries_response_order_order_item_identifier_code_instance.to_dict()
# create an instance of DeliveriesResponseOrderOrderItemIdentifierCode from a dict
deliveries_response_order_order_item_identifier_code_from_dict = DeliveriesResponseOrderOrderItemIdentifierCode.from_dict(deliveries_response_order_order_item_identifier_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


