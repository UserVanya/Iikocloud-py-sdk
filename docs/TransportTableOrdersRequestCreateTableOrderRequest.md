# TransportTableOrdersRequestCreateTableOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Front group ID an order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**order** | [**TransportTableOrdersRequestTableOrder**](TransportTableOrdersRequestTableOrder.md) | Order. | [optional] 
**create_order_settings** | [**TransportTableOrdersRequestCreateTableOrderSettings**](TransportTableOrdersRequestCreateTableOrderSettings.md) | Order creation parameters. | [optional] 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_create_table_order_request import TransportTableOrdersRequestCreateTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestCreateTableOrderRequest from a JSON string
transport_table_orders_request_create_table_order_request_instance = TransportTableOrdersRequestCreateTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestCreateTableOrderRequest.to_json())

# convert the object into a dict
transport_table_orders_request_create_table_order_request_dict = transport_table_orders_request_create_table_order_request_instance.to_dict()
# create an instance of TransportTableOrdersRequestCreateTableOrderRequest from a dict
transport_table_orders_request_create_table_order_request_from_dict = TransportTableOrdersRequestCreateTableOrderRequest.from_dict(transport_table_orders_request_create_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


