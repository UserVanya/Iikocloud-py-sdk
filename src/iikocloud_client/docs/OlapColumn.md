# OlapColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_aggregate** | **bool** | Whether aggregation is allowed for the column | [optional] 
**can_filter** | **bool** | Whether filtering is allowed for the column | [optional] 
**can_group** | **bool** | Whether grouping is allowed for the column | [optional] 
**display_name** | **str** | Report column name | [optional] 
**name** | **str** | Field name (&#x60;FieldName&#x60;): used in &#x60;groupByRowFields&#x60;/&#x60;groupByColFields&#x60;/&#x60;aggregateFields&#x60;, grouping and filters | [optional] 
**tags** | **List[str]** | Report categories the field belongs to | [optional] 
**type** | **str** | Field type (&#x60;ENUM&#x60;, &#x60;STRING&#x60;, &#x60;ID&#x60;, &#x60;DATETIME&#x60;, &#x60;INTEGER&#x60;, &#x60;PERCENT&#x60;, &#x60;DURATION_IN_SECONDS&#x60;, etc.) | [optional] 

## Example

```python
from iikocloud_client.models.olap_column import OlapColumn

# TODO update the JSON string below
json = "{}"
# create an instance of OlapColumn from a JSON string
olap_column_instance = OlapColumn.from_json(json)
# print the JSON string representation of the object
print(OlapColumn.to_json())

# convert the object into a dict
olap_column_dict = olap_column_instance.to_dict()
# create an instance of OlapColumn from a dict
olap_column_from_dict = OlapColumn.from_dict(olap_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


