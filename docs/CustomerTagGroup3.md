# CustomerTagGroup3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**select_several_tags** | **bool** |  | [optional] [default to False]
**items** | [**List[CustomerTagItem3]**](CustomerTagItem3.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.customer_tag_group3 import CustomerTagGroup3

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerTagGroup3 from a JSON string
customer_tag_group3_instance = CustomerTagGroup3.from_json(json)
# print the JSON string representation of the object
print(CustomerTagGroup3.to_json())

# convert the object into a dict
customer_tag_group3_dict = customer_tag_group3_instance.to_dict()
# create an instance of CustomerTagGroup3 from a dict
customer_tag_group3_from_dict = CustomerTagGroup3.from_dict(customer_tag_group3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


