# ComboDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Combo name | 
**price** | **float** | Combo price, if price strategy is fixed | [optional] 
**groups** | [**List[ComboGroupDto]**](ComboGroupDto.md) |  | [optional] 
**image** | [**List[ComboDtoImageInner]**](ComboDtoImageInner.md) | Combo image | 
**description** | **str** | Combo description | [optional] [default to '']
**sizes** | [**List[ComboSizeDto]**](ComboSizeDto.md) | Available sizes for combo (can be empty) | [optional] 
**price_strategy** | **str** |  | 
**start_date** | **str** | The date when the combo will be available until | 
**expiration_date** | **str** | The date when the combo will be available until | 
**id** | **UUID** | Combo id | 

## Example

```python
from iikocloud_client.models.combo_dto import ComboDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComboDto from a JSON string
combo_dto_instance = ComboDto.from_json(json)
# print the JSON string representation of the object
print(ComboDto.to_json())

# convert the object into a dict
combo_dto_dict = combo_dto_instance.to_dict()
# create an instance of ComboDto from a dict
combo_dto_from_dict = ComboDto.from_dict(combo_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


