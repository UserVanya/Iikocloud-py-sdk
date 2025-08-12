# TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest

Request for change time when client wants the order to be delivered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**new_complete_before** | **str** | New time when client wants the order to be delivered (Local for delivery terminal). | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_change_complete_before_request import TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest from a JSON string
transport_deliveries_request_update_order_change_complete_before_request_instance = TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_complete_before_request_dict = transport_deliveries_request_update_order_change_complete_before_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest from a dict
transport_deliveries_request_update_order_change_complete_before_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.from_dict(transport_deliveries_request_update_order_change_complete_before_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


