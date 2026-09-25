# NomenclatureGroupV1Filter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name for filtering | [optional] 
**op** | **str** | Comparison operator: \&quot;eq\&quot; (equal), \&quot;ne\&quot; (not equal), \&quot;gt\&quot; (greater than), \&quot;gte\&quot; (greater than or equal), \&quot;lt\&quot; (less than), \&quot;lte\&quot; (less than or equal), \&quot;in\&quot; (value in list — uses values[]), \&quot;nin\&quot; (value not in list — uses values[]), \&quot;like\&quot; (case-insensitive substring), \&quot;blank\&quot; (null or empty string), \&quot;notblank\&quot; (not null and not empty string) | [optional] 
**value** | **object** | Scalar value for filtering (used with eq, ne, gt, gte, lt, lte, like) | [optional] 
**values** | **List[object]** | Array of values for multi-value filtering (used with \&quot;in\&quot;, \&quot;nin\&quot;) | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_v1_filter import NomenclatureGroupV1Filter

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupV1Filter from a JSON string
nomenclature_group_v1_filter_instance = NomenclatureGroupV1Filter.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupV1Filter.to_json())

# convert the object into a dict
nomenclature_group_v1_filter_dict = nomenclature_group_v1_filter_instance.to_dict()
# create an instance of NomenclatureGroupV1Filter from a dict
nomenclature_group_v1_filter_from_dict = NomenclatureGroupV1Filter.from_dict(nomenclature_group_v1_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


