# AddCustomerToTableOrderRequest

Request for adding customer to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**TableOrderCustomer**](TableOrderCustomer.md) | Guest info. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.add_customer_to_table_order_request import AddCustomerToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomerToTableOrderRequest from a JSON string
add_customer_to_table_order_request_instance = AddCustomerToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomerToTableOrderRequest.to_json())

# convert the object into a dict
add_customer_to_table_order_request_dict = add_customer_to_table_order_request_instance.to_dict()
# create an instance of AddCustomerToTableOrderRequest from a dict
add_customer_to_table_order_request_from_dict = AddCustomerToTableOrderRequest.from_dict(add_customer_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


