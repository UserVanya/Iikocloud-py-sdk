# DeliveryOrderResponseType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**order_service_type** | [**DeliveryServiceType**](DeliveryServiceType.md) | Order type. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_type import DeliveryOrderResponseType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseType from a JSON string
delivery_order_response_type_instance = DeliveryOrderResponseType.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseType.to_json())

# convert the object into a dict
delivery_order_response_type_dict = delivery_order_response_type_instance.to_dict()
# create an instance of DeliveryOrderResponseType from a dict
delivery_order_response_type_from_dict = DeliveryOrderResponseType.from_dict(delivery_order_response_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


