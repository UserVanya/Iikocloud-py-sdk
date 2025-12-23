# DeliveriesResponseOrderCity

City.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_city import DeliveriesResponseOrderCity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCity from a JSON string
deliveries_response_order_city_instance = DeliveriesResponseOrderCity.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCity.to_json())

# convert the object into a dict
deliveries_response_order_city_dict = deliveries_response_order_city_instance.to_dict()
# create an instance of DeliveriesResponseOrderCity from a dict
deliveries_response_order_city_from_dict = DeliveriesResponseOrderCity.from_dict(deliveries_response_order_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


