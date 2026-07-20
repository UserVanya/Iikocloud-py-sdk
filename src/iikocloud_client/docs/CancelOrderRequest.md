# CancelOrderRequest

Request for cancel the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_cause_id** | **UUID** | Cancel order dictionary item id.   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 
**cancel_comment** | **str** | Comment to the delivery cancellation.   &gt; Allowed from version &#x60;8.7.6&#x60;. | [optional] 
**moved_order_id** | **UUID** | Fill this field with id of the new order if current order has been moved to the new RMS/terminal group. | [optional] 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**removal_comment** | **str** | Comment to the charge-off.   &gt; Allowed from version &#x60;8.7.6&#x60;. | [optional] 
**removal_type_id** | **UUID** | Removal type (for delete printed order items).   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 
**user_id_for_writeoff** | **UUID** | User for writeoff (for delete printed order items).   &gt; Allowed from version &#x60;7.7.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.cancel_order_request import CancelOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelOrderRequest from a JSON string
cancel_order_request_instance = CancelOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CancelOrderRequest.to_json())

# convert the object into a dict
cancel_order_request_dict = cancel_order_request_instance.to_dict()
# create an instance of CancelOrderRequest from a dict
cancel_order_request_from_dict = CancelOrderRequest.from_dict(cancel_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


