# DeliveryOrderResponseRegion

Delivery district (part of delivery address).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_region import DeliveryOrderResponseRegion

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseRegion from a JSON string
delivery_order_response_region_instance = DeliveryOrderResponseRegion.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseRegion.to_json())

# convert the object into a dict
delivery_order_response_region_dict = delivery_order_response_region_instance.to_dict()
# create an instance of DeliveryOrderResponseRegion from a dict
delivery_order_response_region_from_dict = DeliveryOrderResponseRegion.from_dict(delivery_order_response_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


