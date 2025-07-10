# TransportDeliveriesResponseOrderProduct

Item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_product import TransportDeliveriesResponseOrderProduct

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderProduct from a JSON string
transport_deliveries_response_order_product_instance = TransportDeliveriesResponseOrderProduct.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderProduct.to_json())

# convert the object into a dict
transport_deliveries_response_order_product_dict = transport_deliveries_response_order_product_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderProduct from a dict
transport_deliveries_response_order_product_from_dict = TransportDeliveriesResponseOrderProduct.from_dict(transport_deliveries_response_order_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


