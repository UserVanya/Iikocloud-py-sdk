# TransportDeliveriesResponseOrderRemovalType

Write-off type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_removal_type import TransportDeliveriesResponseOrderRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderRemovalType from a JSON string
transport_deliveries_response_order_removal_type_instance = TransportDeliveriesResponseOrderRemovalType.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderRemovalType.to_json())

# convert the object into a dict
transport_deliveries_response_order_removal_type_dict = transport_deliveries_response_order_removal_type_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderRemovalType from a dict
transport_deliveries_response_order_removal_type_from_dict = TransportDeliveriesResponseOrderRemovalType.from_dict(transport_deliveries_response_order_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


