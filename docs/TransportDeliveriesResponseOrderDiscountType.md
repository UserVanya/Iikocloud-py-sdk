# TransportDeliveriesResponseOrderDiscountType

Discount type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_discount_type import TransportDeliveriesResponseOrderDiscountType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderDiscountType from a JSON string
transport_deliveries_response_order_discount_type_instance = TransportDeliveriesResponseOrderDiscountType.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderDiscountType.to_json())

# convert the object into a dict
transport_deliveries_response_order_discount_type_dict = transport_deliveries_response_order_discount_type_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderDiscountType from a dict
transport_deliveries_response_order_discount_type_from_dict = TransportDeliveriesResponseOrderDiscountType.from_dict(transport_deliveries_response_order_discount_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


