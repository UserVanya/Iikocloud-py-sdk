# ComboDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Combo name | 
**price** | **float** | Combo price, if price strategy is fixed | [optional] 
**groups** | [**List[ComboGroupDto2]**](ComboGroupDto2.md) |  | [optional] 
**image** | [**List[ComboDto2ImageInner]**](ComboDto2ImageInner.md) | Combo image | 
**description** | **str** | Combo description | [optional] [default to '']
**sizes** | [**List[ComboSizeDto2]**](ComboSizeDto2.md) | Available sizes for combo (can be empty) | [optional] 
**price_strategy** | **str** |  | 
**start_date** | **str** | The date when the combo will be available until | 
**expiration_date** | **str** | The date when the combo will be available until | 
**id** | **UUID** | Combo id | 

## Example

```python
from iikocloud_client.models.combo_dto2 import ComboDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ComboDto2 from a JSON string
combo_dto2_instance = ComboDto2.from_json(json)
# print the JSON string representation of the object
print(ComboDto2.to_json())

# convert the object into a dict
combo_dto2_dict = combo_dto2_instance.to_dict()
# create an instance of ComboDto2 from a dict
combo_dto2_from_dict = ComboDto2.from_dict(combo_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


