# DeliveriesResponseOrderExternalCourierService

ECS info (external courier service).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ECS setting record id. Unique through all organizations. | 
**name** | **str** | ECS name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_external_courier_service import DeliveriesResponseOrderExternalCourierService

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderExternalCourierService from a JSON string
deliveries_response_order_external_courier_service_instance = DeliveriesResponseOrderExternalCourierService.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderExternalCourierService.to_json())

# convert the object into a dict
deliveries_response_order_external_courier_service_dict = deliveries_response_order_external_courier_service_instance.to_dict()
# create an instance of DeliveriesResponseOrderExternalCourierService from a dict
deliveries_response_order_external_courier_service_from_dict = DeliveriesResponseOrderExternalCourierService.from_dict(deliveries_response_order_external_courier_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


