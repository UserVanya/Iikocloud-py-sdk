# OlapPreset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the saved OLAP preset set by the restaurant owner | [optional] 
**preset_id** | **str** | Identifier of the saved OLAP preset; used in the &#x60;olap/presets/get&#x60; method to retrieve its data | [optional] 

## Example

```python
from iikocloud_client.models.olap_preset import OlapPreset

# TODO update the JSON string below
json = "{}"
# create an instance of OlapPreset from a JSON string
olap_preset_instance = OlapPreset.from_json(json)
# print the JSON string representation of the object
print(OlapPreset.to_json())

# convert the object into a dict
olap_preset_dict = olap_preset_instance.to_dict()
# create an instance of OlapPreset from a dict
olap_preset_from_dict = OlapPreset.from_dict(olap_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


