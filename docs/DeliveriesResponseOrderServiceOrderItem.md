# DeliveriesResponseOrderServiceOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**DeliveriesResponseOrderProduct**](DeliveriesResponseOrderProduct.md) | Item. | 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_service_order_item import DeliveriesResponseOrderServiceOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderServiceOrderItem from a JSON string
deliveries_response_order_service_order_item_instance = DeliveriesResponseOrderServiceOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderServiceOrderItem.to_json())

# convert the object into a dict
deliveries_response_order_service_order_item_dict = deliveries_response_order_service_order_item_instance.to_dict()
# create an instance of DeliveriesResponseOrderServiceOrderItem from a dict
deliveries_response_order_service_order_item_from_dict = DeliveriesResponseOrderServiceOrderItem.from_dict(deliveries_response_order_service_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


