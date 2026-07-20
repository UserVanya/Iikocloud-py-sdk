# DeliveryOrderResponseTipsType

The tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/api/1/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_tips_type import DeliveryOrderResponseTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseTipsType from a JSON string
delivery_order_response_tips_type_instance = DeliveryOrderResponseTipsType.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseTipsType.to_json())

# convert the object into a dict
delivery_order_response_tips_type_dict = delivery_order_response_tips_type_instance.to_dict()
# create an instance of DeliveryOrderResponseTipsType from a dict
delivery_order_response_tips_type_from_dict = DeliveryOrderResponseTipsType.from_dict(delivery_order_response_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


