# PlaceType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.place_type import PlaceType

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceType from a JSON string
place_type_instance = PlaceType.from_json(json)
# print the JSON string representation of the object
print(PlaceType.to_json())

# convert the object into a dict
place_type_dict = place_type_instance.to_dict()
# create an instance of PlaceType from a dict
place_type_from_dict = PlaceType.from_dict(place_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


