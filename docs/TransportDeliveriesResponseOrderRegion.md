# TransportDeliveriesResponseOrderRegion

Delivery district (part of delivery address).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_region import TransportDeliveriesResponseOrderRegion

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderRegion from a JSON string
transport_deliveries_response_order_region_instance = TransportDeliveriesResponseOrderRegion.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderRegion.to_json())

# convert the object into a dict
transport_deliveries_response_order_region_dict = transport_deliveries_response_order_region_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderRegion from a dict
transport_deliveries_response_order_region_from_dict = TransportDeliveriesResponseOrderRegion.from_dict(transport_deliveries_response_order_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


