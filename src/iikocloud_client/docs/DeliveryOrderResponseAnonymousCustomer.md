# DeliveryOrderResponseAnonymousCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_anonymous_customer import DeliveryOrderResponseAnonymousCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseAnonymousCustomer from a JSON string
delivery_order_response_anonymous_customer_instance = DeliveryOrderResponseAnonymousCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseAnonymousCustomer.to_json())

# convert the object into a dict
delivery_order_response_anonymous_customer_dict = delivery_order_response_anonymous_customer_instance.to_dict()
# create an instance of DeliveryOrderResponseAnonymousCustomer from a dict
delivery_order_response_anonymous_customer_from_dict = DeliveryOrderResponseAnonymousCustomer.from_dict(delivery_order_response_anonymous_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


