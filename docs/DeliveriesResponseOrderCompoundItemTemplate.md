# DeliveriesResponseOrderCompoundItemTemplate

Modifier scheme information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_compound_item_template import DeliveriesResponseOrderCompoundItemTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCompoundItemTemplate from a JSON string
deliveries_response_order_compound_item_template_instance = DeliveriesResponseOrderCompoundItemTemplate.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCompoundItemTemplate.to_json())

# convert the object into a dict
deliveries_response_order_compound_item_template_dict = deliveries_response_order_compound_item_template_instance.to_dict()
# create an instance of DeliveriesResponseOrderCompoundItemTemplate from a dict
deliveries_response_order_compound_item_template_from_dict = DeliveriesResponseOrderCompoundItemTemplate.from_dict(deliveries_response_order_compound_item_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


