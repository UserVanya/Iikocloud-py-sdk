# IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest

Request for init orders on table by POS orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**pos_order_ids** | **List[UUID]** | POS order IDs. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request import IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest from a JSON string
iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request_instance = IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request_dict = iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest from a dict
iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request_from_dict = IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest.from_dict(iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


