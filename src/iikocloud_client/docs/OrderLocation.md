# OrderLocation

Order location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.order_location import OrderLocation

# TODO update the JSON string below
json = "{}"
# create an instance of OrderLocation from a JSON string
order_location_instance = OrderLocation.from_json(json)
# print the JSON string representation of the object
print(OrderLocation.to_json())

# convert the object into a dict
order_location_dict = order_location_instance.to_dict()
# create an instance of OrderLocation from a dict
order_location_from_dict = OrderLocation.from_dict(order_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


