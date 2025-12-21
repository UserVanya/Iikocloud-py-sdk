# DeliveriesResponseOrderOrderType

Order type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**order_service_type** | [**DeliveriesCommonOrderServiceType**](DeliveriesCommonOrderServiceType.md) | Order type. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_order_type import DeliveriesResponseOrderOrderType

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderOrderType from a JSON string
deliveries_response_order_order_type_instance = DeliveriesResponseOrderOrderType.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderOrderType.to_json())

# convert the object into a dict
deliveries_response_order_order_type_dict = deliveries_response_order_order_type_instance.to_dict()
# create an instance of DeliveriesResponseOrderOrderType from a dict
deliveries_response_order_order_type_from_dict = DeliveriesResponseOrderOrderType.from_dict(deliveries_response_order_order_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


