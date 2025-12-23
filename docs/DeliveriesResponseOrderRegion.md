# DeliveriesResponseOrderRegion

Delivery district (part of delivery address).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_region import DeliveriesResponseOrderRegion

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderRegion from a JSON string
deliveries_response_order_region_instance = DeliveriesResponseOrderRegion.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderRegion.to_json())

# convert the object into a dict
deliveries_response_order_region_dict = deliveries_response_order_region_instance.to_dict()
# create an instance of DeliveriesResponseOrderRegion from a dict
deliveries_response_order_region_from_dict = DeliveriesResponseOrderRegion.from_dict(deliveries_response_order_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


