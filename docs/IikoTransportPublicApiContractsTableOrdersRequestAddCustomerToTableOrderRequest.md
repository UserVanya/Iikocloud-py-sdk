# IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest

Request for adding customer to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**customer** | [**IikoTransportPublicApiContractsTableOrdersRequestTableOrderCustomer**](IikoTransportPublicApiContractsTableOrdersRequestTableOrderCustomer.md) | Guest info. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest from a JSON string
iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request_instance = IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request_dict = iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest from a dict
iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request_from_dict = IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest.from_dict(iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


