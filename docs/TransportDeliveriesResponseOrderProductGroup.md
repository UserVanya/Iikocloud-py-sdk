# TransportDeliveriesResponseOrderProductGroup

Item category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_product_group import TransportDeliveriesResponseOrderProductGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderProductGroup from a JSON string
transport_deliveries_response_order_product_group_instance = TransportDeliveriesResponseOrderProductGroup.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderProductGroup.to_json())

# convert the object into a dict
transport_deliveries_response_order_product_group_dict = transport_deliveries_response_order_product_group_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderProductGroup from a dict
transport_deliveries_response_order_product_group_from_dict = TransportDeliveriesResponseOrderProductGroup.from_dict(transport_deliveries_response_order_product_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


