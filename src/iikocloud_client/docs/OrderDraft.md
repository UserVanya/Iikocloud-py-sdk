# OrderDraft

Order draft object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Draft creation time (UTC). | 
**id** | **UUID** | Order ID. | 
**locked_at** | **str** | Timestamp of when the draft was taken for editing (lock). | [optional] 
**locked_by_user** | **UUID** | ID of the employee, who is editing this draft. | [optional] 
**order** | [**DeliveryOrderDraft**](DeliveryOrderDraft.md) | Order. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID. | [optional] 

## Example

```python
from iikocloud_client.models.order_draft import OrderDraft

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDraft from a JSON string
order_draft_instance = OrderDraft.from_json(json)
# print the JSON string representation of the object
print(OrderDraft.to_json())

# convert the object into a dict
order_draft_dict = order_draft_instance.to_dict()
# create an instance of OrderDraft from a dict
order_draft_from_dict = OrderDraft.from_dict(order_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


