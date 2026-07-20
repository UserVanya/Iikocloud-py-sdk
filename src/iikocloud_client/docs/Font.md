# Font

Font.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family** | **str** | Font family. | 
**font_style** | [**FontStyle**](FontStyle.md) | Font style. May be multiple values. | 
**size** | **float** | Font size. | 

## Example

```python
from iikocloud_client.models.font import Font

# TODO update the JSON string below
json = "{}"
# create an instance of Font from a JSON string
font_instance = Font.from_json(json)
# print the JSON string representation of the object
print(Font.to_json())

# convert the object into a dict
font_dict = font_instance.to_dict()
# create an instance of Font from a dict
font_from_dict = Font.from_dict(font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


