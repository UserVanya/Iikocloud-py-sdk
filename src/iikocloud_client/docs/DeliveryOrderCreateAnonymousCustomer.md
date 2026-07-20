# DeliveryOrderCreateAnonymousCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name. | 

## Example

```python
from iikocloud_client.models.delivery_order_create_anonymous_customer import DeliveryOrderCreateAnonymousCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateAnonymousCustomer from a JSON string
delivery_order_create_anonymous_customer_instance = DeliveryOrderCreateAnonymousCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateAnonymousCustomer.to_json())

# convert the object into a dict
delivery_order_create_anonymous_customer_dict = delivery_order_create_anonymous_customer_instance.to_dict()
# create an instance of DeliveryOrderCreateAnonymousCustomer from a dict
delivery_order_create_anonymous_customer_from_dict = DeliveryOrderCreateAnonymousCustomer.from_dict(delivery_order_create_anonymous_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


