# TransportTableOrdersRequestAddCustomerToTableOrderRequest

Request for adding customer to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**customer** | [**TransportTableOrdersRequestTableOrderCustomer**](TransportTableOrdersRequestTableOrderCustomer.md) | Guest info. | 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_add_customer_to_table_order_request import TransportTableOrdersRequestAddCustomerToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestAddCustomerToTableOrderRequest from a JSON string
transport_table_orders_request_add_customer_to_table_order_request_instance = TransportTableOrdersRequestAddCustomerToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestAddCustomerToTableOrderRequest.to_json())

# convert the object into a dict
transport_table_orders_request_add_customer_to_table_order_request_dict = transport_table_orders_request_add_customer_to_table_order_request_instance.to_dict()
# create an instance of TransportTableOrdersRequestAddCustomerToTableOrderRequest from a dict
transport_table_orders_request_add_customer_to_table_order_request_from_dict = TransportTableOrdersRequestAddCustomerToTableOrderRequest.from_dict(transport_table_orders_request_add_customer_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


