# TransportDeliveriesResponseOrderExternalCourierService

ECS info (external courier service).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ECS setting record id. Unique through all organizations. | 
**name** | **str** | ECS name. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_external_courier_service import TransportDeliveriesResponseOrderExternalCourierService

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderExternalCourierService from a JSON string
transport_deliveries_response_order_external_courier_service_instance = TransportDeliveriesResponseOrderExternalCourierService.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderExternalCourierService.to_json())

# convert the object into a dict
transport_deliveries_response_order_external_courier_service_dict = transport_deliveries_response_order_external_courier_service_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderExternalCourierService from a dict
transport_deliveries_response_order_external_courier_service_from_dict = TransportDeliveriesResponseOrderExternalCourierService.from_dict(transport_deliveries_response_order_external_courier_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


