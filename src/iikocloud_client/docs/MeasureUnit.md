# MeasureUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User-defined measure unit code | [optional] 
**full_name** | **str** | Full name of the measure unit (e.g. kilogram) | [optional] 
**id** | **str** | Measure unit identifier (UUID) | [optional] 
**is_deleted** | **bool** | Flag indicating that the measure unit is logically deleted | [optional] 
**name** | **str** | Short display name of the measure unit (e.g. kg) | [optional] 

## Example

```python
from iikocloud_client.models.measure_unit import MeasureUnit

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureUnit from a JSON string
measure_unit_instance = MeasureUnit.from_json(json)
# print the JSON string representation of the object
print(MeasureUnit.to_json())

# convert the object into a dict
measure_unit_dict = measure_unit_instance.to_dict()
# create an instance of MeasureUnit from a dict
measure_unit_from_dict = MeasureUnit.from_dict(measure_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


