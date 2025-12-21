# IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID an order must be sent to.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**order** | [**IikoTransportPublicApiContractsTableOrdersRequestTableOrder**](IikoTransportPublicApiContractsTableOrdersRequestTableOrder.md) | Order. | [optional] 
**create_order_settings** | [**IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings**](IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings.md) | Order creation parameters. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_create_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest from a JSON string
iiko_transport_public_api_contracts_table_orders_request_create_table_order_request_instance = IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_create_table_order_request_dict = iiko_transport_public_api_contracts_table_orders_request_create_table_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest from a dict
iiko_transport_public_api_contracts_table_orders_request_create_table_order_request_from_dict = IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest.from_dict(iiko_transport_public_api_contracts_table_orders_request_create_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


