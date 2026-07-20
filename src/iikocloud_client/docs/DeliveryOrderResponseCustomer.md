# DeliveryOrderResponseCustomer

Delivery customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.delivery_order_response_customer import DeliveryOrderResponseCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseCustomer from a JSON string
delivery_order_response_customer_instance = DeliveryOrderResponseCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseCustomer.to_json())

# convert the object into a dict
delivery_order_response_customer_dict = delivery_order_response_customer_instance.to_dict()
# create an instance of DeliveryOrderResponseCustomer from a dict
delivery_order_response_customer_from_dict = DeliveryOrderResponseCustomer.from_dict(delivery_order_response_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


