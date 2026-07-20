# SelectedCustomerTag4

Customer tags

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_tag_group_id** | **str** | Tag GUID | 
**selected_tag_ids** | **List[object]** | Tag name | [optional] 

## Example

```python
from iikocloud_client.models.selected_customer_tag4 import SelectedCustomerTag4

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCustomerTag4 from a JSON string
selected_customer_tag4_instance = SelectedCustomerTag4.from_json(json)
# print the JSON string representation of the object
print(SelectedCustomerTag4.to_json())

# convert the object into a dict
selected_customer_tag4_dict = selected_customer_tag4_instance.to_dict()
# create an instance of SelectedCustomerTag4 from a dict
selected_customer_tag4_from_dict = SelectedCustomerTag4.from_dict(selected_customer_tag4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


