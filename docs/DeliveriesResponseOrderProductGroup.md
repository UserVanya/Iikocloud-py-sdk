# DeliveriesResponseOrderProductGroup

Item category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_product_group import DeliveriesResponseOrderProductGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderProductGroup from a JSON string
deliveries_response_order_product_group_instance = DeliveriesResponseOrderProductGroup.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderProductGroup.to_json())

# convert the object into a dict
deliveries_response_order_product_group_dict = deliveries_response_order_product_group_instance.to_dict()
# create an instance of DeliveriesResponseOrderProductGroup from a dict
deliveries_response_order_product_group_from_dict = DeliveriesResponseOrderProductGroup.from_dict(deliveries_response_order_product_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


