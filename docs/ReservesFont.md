# ReservesFont

Font.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family** | **str** | Font family. | 
**size** | **float** | Font size. | 
**font_style** | [**ReservesFontStyle**](ReservesFontStyle.md) | Font style. May be multiple values. | 

## Example

```python
from iikocloud_client.models.reserves_font import ReservesFont

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesFont from a JSON string
reserves_font_instance = ReservesFont.from_json(json)
# print the JSON string representation of the object
print(ReservesFont.to_json())

# convert the object into a dict
reserves_font_dict = reserves_font_instance.to_dict()
# create an instance of ReservesFont from a dict
reserves_font_from_dict = ReservesFont.from_dict(reserves_font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


