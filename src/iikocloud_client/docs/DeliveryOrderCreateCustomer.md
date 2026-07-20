# DeliveryOrderCreateCustomer

Customer base info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.delivery_order_create_customer import DeliveryOrderCreateCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateCustomer from a JSON string
delivery_order_create_customer_instance = DeliveryOrderCreateCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateCustomer.to_json())

# convert the object into a dict
delivery_order_create_customer_dict = delivery_order_create_customer_instance.to_dict()
# create an instance of DeliveryOrderCreateCustomer from a dict
delivery_order_create_customer_from_dict = DeliveryOrderCreateCustomer.from_dict(delivery_order_create_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


