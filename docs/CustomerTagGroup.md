# CustomerTagGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**select_several_tags** | **bool** |  | [optional] [default to False]
**items** | [**List[CustomerTagItem]**](CustomerTagItem.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.customer_tag_group import CustomerTagGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerTagGroup from a JSON string
customer_tag_group_instance = CustomerTagGroup.from_json(json)
# print the JSON string representation of the object
print(CustomerTagGroup.to_json())

# convert the object into a dict
customer_tag_group_dict = customer_tag_group_instance.to_dict()
# create an instance of CustomerTagGroup from a dict
customer_tag_group_from_dict = CustomerTagGroup.from_dict(customer_tag_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


