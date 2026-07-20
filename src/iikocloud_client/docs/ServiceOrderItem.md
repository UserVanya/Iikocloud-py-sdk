# ServiceOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 
**service** | [**Product**](Product.md) | Item. | 

## Example

```python
from iikocloud_client.models.service_order_item import ServiceOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceOrderItem from a JSON string
service_order_item_instance = ServiceOrderItem.from_json(json)
# print the JSON string representation of the object
print(ServiceOrderItem.to_json())

# convert the object into a dict
service_order_item_dict = service_order_item_instance.to_dict()
# create an instance of ServiceOrderItem from a dict
service_order_item_from_dict = ServiceOrderItem.from_dict(service_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


