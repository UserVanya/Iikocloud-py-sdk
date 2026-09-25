# FilterCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name for filtering | [optional] 
**op** | **str** | Operation (\&quot;eq\&quot;, \&quot;ne\&quot;, \&quot;gt\&quot;, \&quot;gte\&quot;, \&quot;lt\&quot;, \&quot;lte\&quot;, \&quot;in\&quot;, \&quot;nin\&quot;, \&quot;like\&quot;, \&quot;blank\&quot;, \&quot;notblank\&quot;) | [optional] 
**value** | **object** | Value for filtering by the field | [optional] 

## Example

```python
from iikocloud_client.models.filter_condition import FilterCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FilterCondition from a JSON string
filter_condition_instance = FilterCondition.from_json(json)
# print the JSON string representation of the object
print(FilterCondition.to_json())

# convert the object into a dict
filter_condition_dict = filter_condition_instance.to_dict()
# create an instance of FilterCondition from a dict
filter_condition_from_dict = FilterCondition.from_dict(filter_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


