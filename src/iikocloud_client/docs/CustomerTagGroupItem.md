# CustomerTagGroupItem

Represents a set of selected tags for a specific customer tag group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_tag_group_id** | **UUID** | Customer tag group ID. | 
**selected_tag_ids** | **List[UUID]** | Set of selected tag IDs within the group. | 

## Example

```python
from iikocloud_client.models.customer_tag_group_item import CustomerTagGroupItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerTagGroupItem from a JSON string
customer_tag_group_item_instance = CustomerTagGroupItem.from_json(json)
# print the JSON string representation of the object
print(CustomerTagGroupItem.to_json())

# convert the object into a dict
customer_tag_group_item_dict = customer_tag_group_item_instance.to_dict()
# create an instance of CustomerTagGroupItem from a dict
customer_tag_group_item_from_dict = CustomerTagGroupItem.from_dict(customer_tag_group_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


