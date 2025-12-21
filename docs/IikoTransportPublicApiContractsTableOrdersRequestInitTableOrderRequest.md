# IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest

Request for init orders on table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**table_ids** | **List[UUID]** | Table IDs.                Can be obtained by &#x60;/reserve/available_restaurant_sections&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_init_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest from a JSON string
iiko_transport_public_api_contracts_table_orders_request_init_table_order_request_instance = IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_init_table_order_request_dict = iiko_transport_public_api_contracts_table_orders_request_init_table_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest from a dict
iiko_transport_public_api_contracts_table_orders_request_init_table_order_request_from_dict = IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest.from_dict(iiko_transport_public_api_contracts_table_orders_request_init_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


