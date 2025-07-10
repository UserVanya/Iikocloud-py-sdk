# TransportDeliveriesRequestUpdateOrderCourierRequest

Request for order courier update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**employee_id** | **str** | Courier ID.                Can be obtained by &#x60;/api/1/employees/couriers&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_courier_request import TransportDeliveriesRequestUpdateOrderCourierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderCourierRequest from a JSON string
transport_deliveries_request_update_order_courier_request_instance = TransportDeliveriesRequestUpdateOrderCourierRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderCourierRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_courier_request_dict = transport_deliveries_request_update_order_courier_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderCourierRequest from a dict
transport_deliveries_request_update_order_courier_request_from_dict = TransportDeliveriesRequestUpdateOrderCourierRequest.from_dict(transport_deliveries_request_update_order_courier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


