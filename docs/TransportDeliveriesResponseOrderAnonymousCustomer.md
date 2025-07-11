# TransportDeliveriesResponseOrderAnonymousCustomer

'One-time' customer:  - should be used if a customer does not agree to take part in the store's loyalty programs or an aggregator (external system) does not provide customer details  - customer details will NOT be added to the store's customer database and will be used ONLY to complete the current order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_anonymous_customer import TransportDeliveriesResponseOrderAnonymousCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderAnonymousCustomer from a JSON string
transport_deliveries_response_order_anonymous_customer_instance = TransportDeliveriesResponseOrderAnonymousCustomer.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderAnonymousCustomer.to_json())

# convert the object into a dict
transport_deliveries_response_order_anonymous_customer_dict = transport_deliveries_response_order_anonymous_customer_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderAnonymousCustomer from a dict
transport_deliveries_response_order_anonymous_customer_from_dict = TransportDeliveriesResponseOrderAnonymousCustomer.from_dict(transport_deliveries_response_order_anonymous_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


