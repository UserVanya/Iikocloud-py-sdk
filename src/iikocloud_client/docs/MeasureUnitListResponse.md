# MeasureUnitListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[MeasureUnit]**](MeasureUnit.md) | List of entities | [optional] 
**limit** | **int** | Limit value from the request | [optional] 
**offset** | **int** | Offset value from the request | [optional] 
**total_count** | **int** | Total number of records matching the filter | [optional] 

## Example

```python
from iikocloud_client.models.measure_unit_list_response import MeasureUnitListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureUnitListResponse from a JSON string
measure_unit_list_response_instance = MeasureUnitListResponse.from_json(json)
# print the JSON string representation of the object
print(MeasureUnitListResponse.to_json())

# convert the object into a dict
measure_unit_list_response_dict = measure_unit_list_response_instance.to_dict()
# create an instance of MeasureUnitListResponse from a dict
measure_unit_list_response_from_dict = MeasureUnitListResponse.from_dict(measure_unit_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


