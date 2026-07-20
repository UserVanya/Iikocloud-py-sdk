# DeliveryOrderResponseStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | [**DeliveryOrderResponseCity**](DeliveryOrderResponseCity.md) | City. | 
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_street import DeliveryOrderResponseStreet

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseStreet from a JSON string
delivery_order_response_street_instance = DeliveryOrderResponseStreet.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseStreet.to_json())

# convert the object into a dict
delivery_order_response_street_dict = delivery_order_response_street_instance.to_dict()
# create an instance of DeliveryOrderResponseStreet from a dict
delivery_order_response_street_from_dict = DeliveryOrderResponseStreet.from_dict(delivery_order_response_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


