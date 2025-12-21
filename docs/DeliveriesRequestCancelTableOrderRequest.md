# DeliveriesRequestCancelTableOrderRequest

Request to cancel a table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**removal_type_id** | **UUID** | Removal type (used during deletion of printed order items). | [optional] 
**removal_comment** | **str** | Comment to the charge-off. | [optional] 
**user_id_for_writeoff** | **UUID** | User for writeoff (used during deletion of printed order items). | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_cancel_table_order_request import DeliveriesRequestCancelTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCancelTableOrderRequest from a JSON string
deliveries_request_cancel_table_order_request_instance = DeliveriesRequestCancelTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCancelTableOrderRequest.to_json())

# convert the object into a dict
deliveries_request_cancel_table_order_request_dict = deliveries_request_cancel_table_order_request_instance.to_dict()
# create an instance of DeliveriesRequestCancelTableOrderRequest from a dict
deliveries_request_cancel_table_order_request_from_dict = DeliveriesRequestCancelTableOrderRequest.from_dict(deliveries_request_cancel_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


