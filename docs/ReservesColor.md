# ReservesColor

Color.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a** | **int** | Alpha-component. | 
**r** | **int** | Red-component. | 
**g** | **int** | Green-component. | 
**b** | **int** | Blue-component. | 

## Example

```python
from iikocloud_client.models.reserves_color import ReservesColor

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesColor from a JSON string
reserves_color_instance = ReservesColor.from_json(json)
# print the JSON string representation of the object
print(ReservesColor.to_json())

# convert the object into a dict
reserves_color_dict = reserves_color_instance.to_dict()
# create an instance of ReservesColor from a dict
reserves_color_from_dict = ReservesColor.from_dict(reserves_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


