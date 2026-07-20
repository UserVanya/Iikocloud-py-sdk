# InitTableOrderByPosOrderRequest

Request for init orders on table by POS orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**pos_order_ids** | **List[UUID]** | POS order IDs. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.init_table_order_by_pos_order_request import InitTableOrderByPosOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitTableOrderByPosOrderRequest from a JSON string
init_table_order_by_pos_order_request_instance = InitTableOrderByPosOrderRequest.from_json(json)
# print the JSON string representation of the object
print(InitTableOrderByPosOrderRequest.to_json())

# convert the object into a dict
init_table_order_by_pos_order_request_dict = init_table_order_by_pos_order_request_instance.to_dict()
# create an instance of InitTableOrderByPosOrderRequest from a dict
init_table_order_by_pos_order_request_from_dict = InitTableOrderByPosOrderRequest.from_dict(init_table_order_by_pos_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


