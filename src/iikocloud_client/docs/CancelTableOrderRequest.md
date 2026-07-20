# CancelTableOrderRequest

Request to cancel a table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**removal_comment** | **str** | Comment to the charge-off. | [optional] 
**removal_type_id** | **UUID** | Removal type (used during deletion of printed order items). | [optional] 
**user_id_for_writeoff** | **UUID** | User for writeoff (used during deletion of printed order items). | [optional] 

## Example

```python
from iikocloud_client.models.cancel_table_order_request import CancelTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelTableOrderRequest from a JSON string
cancel_table_order_request_instance = CancelTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CancelTableOrderRequest.to_json())

# convert the object into a dict
cancel_table_order_request_dict = cancel_table_order_request_instance.to_dict()
# create an instance of CancelTableOrderRequest from a dict
cancel_table_order_request_from_dict = CancelTableOrderRequest.from_dict(cancel_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


