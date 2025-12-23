# DeliveriesResponseOrderRemovalType

Write-off type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_removal_type import DeliveriesResponseOrderRemovalType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderRemovalType from a JSON string
deliveries_response_order_removal_type_instance = DeliveriesResponseOrderRemovalType.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderRemovalType.to_json())

# convert the object into a dict
deliveries_response_order_removal_type_dict = deliveries_response_order_removal_type_instance.to_dict()
# create an instance of DeliveriesResponseOrderRemovalType from a dict
deliveries_response_order_removal_type_from_dict = DeliveriesResponseOrderRemovalType.from_dict(deliveries_response_order_removal_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


