# CommonExternalData

External data key and value pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | External data key. | 
**value** | **str** | External data value. | 

## Example

```python
from iikocloud_client.models.common_external_data import CommonExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of CommonExternalData from a JSON string
common_external_data_instance = CommonExternalData.from_json(json)
# print the JSON string representation of the object
print(CommonExternalData.to_json())

# convert the object into a dict
common_external_data_dict = common_external_data_instance.to_dict()
# create an instance of CommonExternalData from a dict
common_external_data_from_dict = CommonExternalData.from_dict(common_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


