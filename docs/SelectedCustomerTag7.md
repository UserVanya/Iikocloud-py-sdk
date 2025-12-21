# SelectedCustomerTag7

Customer tags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_tag_group_id** | **str** | Tag GUID | 
**selected_tag_ids** | **List[object]** | Tag name | [optional] 

## Example

```python
from iikocloud_client.models.selected_customer_tag7 import SelectedCustomerTag7

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCustomerTag7 from a JSON string
selected_customer_tag7_instance = SelectedCustomerTag7.from_json(json)
# print the JSON string representation of the object
print(SelectedCustomerTag7.to_json())

# convert the object into a dict
selected_customer_tag7_dict = selected_customer_tag7_instance.to_dict()
# create an instance of SelectedCustomerTag7 from a dict
selected_customer_tag7_from_dict = SelectedCustomerTag7.from_dict(selected_customer_tag7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


