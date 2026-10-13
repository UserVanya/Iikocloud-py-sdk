# OlapPresetReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Start of the report period (inclusive) in &#x60;yyyy-MM-dd&#x60; format | 
**date_to** | **str** | End of the report period (exclusive) in &#x60;yyyy-MM-dd&#x60; format | 
**preset_id** | **str** | Identifier of the saved OLAP preset (from &#x60;olap/presets/list&#x60;) | 

## Example

```python
from iikocloud_client.models.olap_preset_report_request import OlapPresetReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OlapPresetReportRequest from a JSON string
olap_preset_report_request_instance = OlapPresetReportRequest.from_json(json)
# print the JSON string representation of the object
print(OlapPresetReportRequest.to_json())

# convert the object into a dict
olap_preset_report_request_dict = olap_preset_report_request_instance.to_dict()
# create an instance of OlapPresetReportRequest from a dict
olap_preset_report_request_from_dict = OlapPresetReportRequest.from_dict(olap_preset_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


