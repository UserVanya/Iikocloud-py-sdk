# DeliveriesRequestCreateOrderAnonymousCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name. | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_anonymous_customer import DeliveriesRequestCreateOrderAnonymousCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderAnonymousCustomer from a JSON string
deliveries_request_create_order_anonymous_customer_instance = DeliveriesRequestCreateOrderAnonymousCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderAnonymousCustomer.to_json())

# convert the object into a dict
deliveries_request_create_order_anonymous_customer_dict = deliveries_request_create_order_anonymous_customer_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderAnonymousCustomer from a dict
deliveries_request_create_order_anonymous_customer_from_dict = DeliveriesRequestCreateOrderAnonymousCustomer.from_dict(deliveries_request_create_order_anonymous_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


