# DeliveriesResponseOrderTipsType

The tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_tips_type import DeliveriesResponseOrderTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderTipsType from a JSON string
deliveries_response_order_tips_type_instance = DeliveriesResponseOrderTipsType.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderTipsType.to_json())

# convert the object into a dict
deliveries_response_order_tips_type_dict = deliveries_response_order_tips_type_instance.to_dict()
# create an instance of DeliveriesResponseOrderTipsType from a dict
deliveries_response_order_tips_type_from_dict = DeliveriesResponseOrderTipsType.from_dict(deliveries_response_order_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


