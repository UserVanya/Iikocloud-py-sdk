# DeliveryOrderResponseExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key. | 
**value** | **str** | Public. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_external_data import DeliveryOrderResponseExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseExternalData from a JSON string
delivery_order_response_external_data_instance = DeliveryOrderResponseExternalData.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseExternalData.to_json())

# convert the object into a dict
delivery_order_response_external_data_dict = delivery_order_response_external_data_instance.to_dict()
# create an instance of DeliveryOrderResponseExternalData from a dict
delivery_order_response_external_data_from_dict = DeliveryOrderResponseExternalData.from_dict(delivery_order_response_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


