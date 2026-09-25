# OlapFilterDoc

One item of the filters array. Which fields are actually present depends on `filterType`: name and `filterType` are always present; `values` — for IncludeValues/ExcludeValues; `from`/`to` — a number for `Range` or a date/time string (ISO 8601) for `DateRange`; `periodType` — for `DateRange`; `includeLow`/`includeHigh` — for `Range` and `DateRange`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_type** | **str** | Filter type: &#x60;IncludeValues&#x60;/&#x60;ExcludeValues&#x60; — by values, &#x60;Range&#x60; — by numeric range, &#x60;DateRange&#x60; — by date range | 
**var_from** | **object** | Lower range bound: a number (&#x60;Range&#x60;) or a date (&#x60;DateRange&#x60;) in one of &#x60;yyyy-MM-dd&#x60;, &#x60;yyyy-MM-ddTHH:mm&#x60;, &#x60;yyyy-MM-ddTHH:mm:ss&#x60; formats. For periodType &#x3D; CUSTOM the period is limited to 31 days inclusive. | [optional] 
**include_high** | **bool** | Whether to include the upper range bound; defaults to &#x60;false&#x60; | [optional] 
**include_low** | **bool** | Whether to include the lower range bound; defaults to &#x60;true&#x60; | [optional] 
**name** | **str** | Field name to filter by (&#x60;FieldName&#x60; from &#x60;columns/get&#x60;) | 
**period_type** | **str** | Period type (for &#x60;DateRange&#x60;): &#x60;CUSTOM&#x60;, &#x60;OPEN_PERIOD&#x60;, &#x60;TODAY&#x60;, &#x60;YESTERDAY&#x60;, &#x60;CURRENT_WEEK&#x60;, &#x60;CURRENT_MONTH&#x60;, &#x60;CURRENT_YEAR&#x60;, &#x60;LAST_WEEK&#x60;, &#x60;LAST_MONTH&#x60;, &#x60;LAST_YEAR&#x60; | [optional] 
**to** | **object** | Upper range bound: a number (&#x60;Range&#x60;) or a date (&#x60;DateRange&#x60;) in one of &#x60;yyyy-MM-dd&#x60;, &#x60;yyyy-MM-ddTHH:mm&#x60;, &#x60;yyyy-MM-ddTHH:mm:ss&#x60; formats; required for &#x60;Range&#x60; and for &#x60;DateRange&#x60; with &#x60;periodType&#x3D;CUSTOM&#x60;. For periodType &#x3D; CUSTOM the period is limited to 31 days inclusive. | [optional] 
**values** | **List[str]** | Field values to filter by; required for &#x60;IncludeValues&#x60;/&#x60;ExcludeValues&#x60; &#x60;filterType&#x60; | [optional] 

## Example

```python
from iikocloud_client.models.olap_filter_doc import OlapFilterDoc

# TODO update the JSON string below
json = "{}"
# create an instance of OlapFilterDoc from a JSON string
olap_filter_doc_instance = OlapFilterDoc.from_json(json)
# print the JSON string representation of the object
print(OlapFilterDoc.to_json())

# convert the object into a dict
olap_filter_doc_dict = olap_filter_doc_instance.to_dict()
# create an instance of OlapFilterDoc from a dict
olap_filter_doc_from_dict = OlapFilterDoc.from_dict(olap_filter_doc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


