# TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest

Request for change order's delivery type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_service_type** | **str** |  | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_service_type_request import TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest from a JSON string
transport_deliveries_request_update_order_change_service_type_request_instance = TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_change_service_type_request_dict = transport_deliveries_request_update_order_change_service_type_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest from a dict
transport_deliveries_request_update_order_change_service_type_request_from_dict = TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_dict(transport_deliveries_request_update_order_change_service_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


