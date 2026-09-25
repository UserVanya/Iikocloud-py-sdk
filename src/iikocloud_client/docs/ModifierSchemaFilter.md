# ModifierSchemaFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name for filtering | [optional] 
**op** | **str** | Comparison operator: \&quot;eq\&quot; (equal), \&quot;ne\&quot; (not equal), \&quot;gt\&quot; (greater than), \&quot;gte\&quot; (greater than or equal), \&quot;lt\&quot; (less than), \&quot;lte\&quot; (less than or equal), \&quot;in\&quot; (value in list — uses values[]), \&quot;nin\&quot; (value not in list — uses values[]), \&quot;like\&quot; (case-insensitive substring), \&quot;blank\&quot; (null or empty string), \&quot;notblank\&quot; (not null and not empty string) | [optional] 
**value** | **object** | Scalar value for filtering (used with eq, ne, gt, gte, lt, lte, like) | [optional] 
**values** | **List[object]** | Array of values for multi-value filtering (used with \&quot;in\&quot;, \&quot;nin\&quot;) | [optional] 

## Example

```python
from iikocloud_client.models.modifier_schema_filter import ModifierSchemaFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierSchemaFilter from a JSON string
modifier_schema_filter_instance = ModifierSchemaFilter.from_json(json)
# print the JSON string representation of the object
print(ModifierSchemaFilter.to_json())

# convert the object into a dict
modifier_schema_filter_dict = modifier_schema_filter_instance.to_dict()
# create an instance of ModifierSchemaFilter from a dict
modifier_schema_filter_from_dict = ModifierSchemaFilter.from_dict(modifier_schema_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


