# TransportDeliveriesRequestCreateOrderAnonymousCustomer

'One-time' customer:  - should be used if a customer does not agree to take part in the store's loyalty programs or an aggregator (external system) does not provide customer details  - customer details will NOT be added to the store's customer database and will be used ONLY to complete the current order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_anonymous_customer import TransportDeliveriesRequestCreateOrderAnonymousCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderAnonymousCustomer from a JSON string
transport_deliveries_request_create_order_anonymous_customer_instance = TransportDeliveriesRequestCreateOrderAnonymousCustomer.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderAnonymousCustomer.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_anonymous_customer_dict = transport_deliveries_request_create_order_anonymous_customer_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderAnonymousCustomer from a dict
transport_deliveries_request_create_order_anonymous_customer_from_dict = TransportDeliveriesRequestCreateOrderAnonymousCustomer.from_dict(transport_deliveries_request_create_order_anonymous_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


