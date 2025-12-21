# CustomerTagGroup2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**select_several_tags** | **bool** |  | [optional] [default to False]
**items** | [**List[CustomerTagItem2]**](CustomerTagItem2.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.customer_tag_group2 import CustomerTagGroup2

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerTagGroup2 from a JSON string
customer_tag_group2_instance = CustomerTagGroup2.from_json(json)
# print the JSON string representation of the object
print(CustomerTagGroup2.to_json())

# convert the object into a dict
customer_tag_group2_dict = customer_tag_group2_instance.to_dict()
# create an instance of CustomerTagGroup2 from a dict
customer_tag_group2_from_dict = CustomerTagGroup2.from_dict(customer_tag_group2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


