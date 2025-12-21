# DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest

Request for change time when client wants the order to be delivered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**new_complete_before** | **str** | New time when client wants the order to be delivered (Local for delivery terminal). | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_complete_before_request import DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest from a JSON string
deliveries_request_update_order_change_complete_before_request_instance = DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_change_complete_before_request_dict = deliveries_request_update_order_change_complete_before_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest from a dict
deliveries_request_update_order_change_complete_before_request_from_dict = DeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.from_dict(deliveries_request_update_order_change_complete_before_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


