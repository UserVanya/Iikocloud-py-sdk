# TableOrdersRequestAddCustomerToTableOrderRequest

Request for adding customer to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**customer** | [**TableOrdersRequestTableOrderCustomer**](TableOrdersRequestTableOrderCustomer.md) | Guest info. | 

## Example

```python
from iikocloud_client.models.table_orders_request_add_customer_to_table_order_request import TableOrdersRequestAddCustomerToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestAddCustomerToTableOrderRequest from a JSON string
table_orders_request_add_customer_to_table_order_request_instance = TableOrdersRequestAddCustomerToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestAddCustomerToTableOrderRequest.to_json())

# convert the object into a dict
table_orders_request_add_customer_to_table_order_request_dict = table_orders_request_add_customer_to_table_order_request_instance.to_dict()
# create an instance of TableOrdersRequestAddCustomerToTableOrderRequest from a dict
table_orders_request_add_customer_to_table_order_request_from_dict = TableOrdersRequestAddCustomerToTableOrderRequest.from_dict(table_orders_request_add_customer_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


