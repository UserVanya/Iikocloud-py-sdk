# DeliveryOrderCreateAddress

Order delivery address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.delivery_order_create_address import DeliveryOrderCreateAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateAddress from a JSON string
delivery_order_create_address_instance = DeliveryOrderCreateAddress.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateAddress.to_json())

# convert the object into a dict
delivery_order_create_address_dict = delivery_order_create_address_instance.to_dict()
# create an instance of DeliveryOrderCreateAddress from a dict
delivery_order_create_address_from_dict = DeliveryOrderCreateAddress.from_dict(delivery_order_create_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


