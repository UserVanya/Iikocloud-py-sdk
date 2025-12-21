# DeliveriesRequestCreateOrderCustomer

Customer base info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_customer import DeliveriesRequestCreateOrderCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderCustomer from a JSON string
deliveries_request_create_order_customer_instance = DeliveriesRequestCreateOrderCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderCustomer.to_json())

# convert the object into a dict
deliveries_request_create_order_customer_dict = deliveries_request_create_order_customer_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderCustomer from a dict
deliveries_request_create_order_customer_from_dict = DeliveriesRequestCreateOrderCustomer.from_dict(deliveries_request_create_order_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


