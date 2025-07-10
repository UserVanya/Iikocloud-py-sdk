# TransportTableOrdersRequestInitTableOrderByPosOrderRequest

Request for init orders on table by POS orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**pos_order_ids** | **List[str]** | POS order IDs. | 

## Example

```python
from iiko_cloud_client.models.transport_table_orders_request_init_table_order_by_pos_order_request import TransportTableOrdersRequestInitTableOrderByPosOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestInitTableOrderByPosOrderRequest from a JSON string
transport_table_orders_request_init_table_order_by_pos_order_request_instance = TransportTableOrdersRequestInitTableOrderByPosOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestInitTableOrderByPosOrderRequest.to_json())

# convert the object into a dict
transport_table_orders_request_init_table_order_by_pos_order_request_dict = transport_table_orders_request_init_table_order_by_pos_order_request_instance.to_dict()
# create an instance of TransportTableOrdersRequestInitTableOrderByPosOrderRequest from a dict
transport_table_orders_request_init_table_order_by_pos_order_request_from_dict = TransportTableOrdersRequestInitTableOrderByPosOrderRequest.from_dict(transport_table_orders_request_init_table_order_by_pos_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


