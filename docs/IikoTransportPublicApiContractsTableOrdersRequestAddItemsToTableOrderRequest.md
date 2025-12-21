# IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest

Request for add order items to table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_order_items_settings** | [**IikoTransportPublicApiContractsTableOrdersRequestAddTableOrderItemsSettings**](IikoTransportPublicApiContractsTableOrdersRequestAddTableOrderItemsSettings.md) | Add order items parameters. | [optional] 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest from a JSON string
iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request_instance = IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request_dict = iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest from a dict
iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request_from_dict = IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest.from_dict(iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


