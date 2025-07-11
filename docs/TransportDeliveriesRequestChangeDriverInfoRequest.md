# TransportDeliveriesRequestChangeDriverInfoRequest

Request for change driver info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**driver_id** | **str** | Driver ID.                Can be obtained by &#x60;/api/1/employees/couriers&#x60; operation. | [optional] 
**estimated_time** | **str** | Delivery estimated time. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_change_driver_info_request import TransportDeliveriesRequestChangeDriverInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestChangeDriverInfoRequest from a JSON string
transport_deliveries_request_change_driver_info_request_instance = TransportDeliveriesRequestChangeDriverInfoRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestChangeDriverInfoRequest.to_json())

# convert the object into a dict
transport_deliveries_request_change_driver_info_request_dict = transport_deliveries_request_change_driver_info_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestChangeDriverInfoRequest from a dict
transport_deliveries_request_change_driver_info_request_from_dict = TransportDeliveriesRequestChangeDriverInfoRequest.from_dict(transport_deliveries_request_change_driver_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


