# CoordinateInfo

DTO of map coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**server_timestamp** | **int** | Time of coordinate saving on server in the Unix timestamp format. | 

## Example

```python
from iikocloud_client.models.coordinate_info import CoordinateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CoordinateInfo from a JSON string
coordinate_info_instance = CoordinateInfo.from_json(json)
# print the JSON string representation of the object
print(CoordinateInfo.to_json())

# convert the object into a dict
coordinate_info_dict = coordinate_info_instance.to_dict()
# create an instance of CoordinateInfo from a dict
coordinate_info_from_dict = CoordinateInfo.from_dict(coordinate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


