# CustomerTagItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from iikocloud_client.models.customer_tag_item import CustomerTagItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerTagItem from a JSON string
customer_tag_item_instance = CustomerTagItem.from_json(json)
# print the JSON string representation of the object
print(CustomerTagItem.to_json())

# convert the object into a dict
customer_tag_item_dict = customer_tag_item_instance.to_dict()
# create an instance of CustomerTagItem from a dict
customer_tag_item_from_dict = CustomerTagItem.from_dict(customer_tag_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


