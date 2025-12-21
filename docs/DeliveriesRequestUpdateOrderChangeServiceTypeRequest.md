# DeliveriesRequestUpdateOrderChangeServiceTypeRequest

Request for change order's delivery type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_service_type** | **str** |  | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_change_service_type_request import DeliveriesRequestUpdateOrderChangeServiceTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderChangeServiceTypeRequest from a JSON string
deliveries_request_update_order_change_service_type_request_instance = DeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderChangeServiceTypeRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_change_service_type_request_dict = deliveries_request_update_order_change_service_type_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderChangeServiceTypeRequest from a dict
deliveries_request_update_order_change_service_type_request_from_dict = DeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_dict(deliveries_request_update_order_change_service_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


