# MeasureUnitListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | Filter by deletion status; omit to return all records | [optional] 
**limit** | **int** | Maximum number of records (0 &#x3D; no limit) | [optional] 
**offset** | **int** | Number of records to skip | [optional] 
**revision** | **int** | Return only records with revision &gt;&#x3D; this value | [optional] 

## Example

```python
from iikocloud_client.models.measure_unit_list_request import MeasureUnitListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureUnitListRequest from a JSON string
measure_unit_list_request_instance = MeasureUnitListRequest.from_json(json)
# print the JSON string representation of the object
print(MeasureUnitListRequest.to_json())

# convert the object into a dict
measure_unit_list_request_dict = measure_unit_list_request_instance.to_dict()
# create an instance of MeasureUnitListRequest from a dict
measure_unit_list_request_from_dict = MeasureUnitListRequest.from_dict(measure_unit_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


