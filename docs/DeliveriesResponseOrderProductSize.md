# DeliveriesResponseOrderProductSize

Item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_product_size import DeliveriesResponseOrderProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderProductSize from a JSON string
deliveries_response_order_product_size_instance = DeliveriesResponseOrderProductSize.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderProductSize.to_json())

# convert the object into a dict
deliveries_response_order_product_size_dict = deliveries_response_order_product_size_instance.to_dict()
# create an instance of DeliveriesResponseOrderProductSize from a dict
deliveries_response_order_product_size_from_dict = DeliveriesResponseOrderProductSize.from_dict(deliveries_response_order_product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


