# ButtonImageDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.button_image_dto import ButtonImageDto

# TODO update the JSON string below
json = "{}"
# create an instance of ButtonImageDto from a JSON string
button_image_dto_instance = ButtonImageDto.from_json(json)
# print the JSON string representation of the object
print(ButtonImageDto.to_json())

# convert the object into a dict
button_image_dto_dict = button_image_dto_instance.to_dict()
# create an instance of ButtonImageDto from a dict
button_image_dto_from_dict = ButtonImageDto.from_dict(button_image_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


