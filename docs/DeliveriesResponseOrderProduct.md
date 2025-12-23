# DeliveriesResponseOrderProduct

Item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_product import DeliveriesResponseOrderProduct

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderProduct from a JSON string
deliveries_response_order_product_instance = DeliveriesResponseOrderProduct.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderProduct.to_json())

# convert the object into a dict
deliveries_response_order_product_dict = deliveries_response_order_product_instance.to_dict()
# create an instance of DeliveriesResponseOrderProduct from a dict
deliveries_response_order_product_from_dict = DeliveriesResponseOrderProduct.from_dict(deliveries_response_order_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


