# DeliveryOrderResponseRemovalType

Write-off type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_removal_type import DeliveryOrderResponseRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseRemovalType from a JSON string
delivery_order_response_removal_type_instance = DeliveryOrderResponseRemovalType.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseRemovalType.to_json())

# convert the object into a dict
delivery_order_response_removal_type_dict = delivery_order_response_removal_type_instance.to_dict()
# create an instance of DeliveryOrderResponseRemovalType from a dict
delivery_order_response_removal_type_from_dict = DeliveryOrderResponseRemovalType.from_dict(delivery_order_response_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


