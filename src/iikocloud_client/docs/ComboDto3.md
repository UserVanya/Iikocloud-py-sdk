# ComboDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Combo description | [optional] [default to '']
**expiration_date** | **str** | The date when the combo will be available until | 
**groups** | [**List[ComboGroupDto3]**](ComboGroupDto3.md) |  | [optional] 
**id** | **UUID** | Combo id | 
**image** | [**List[ComboDto3ImageInner]**](ComboDto3ImageInner.md) | Combo image | 
**name** | **str** | Combo name | 
**price** | **float** | Combo price, if price strategy is fixed | [optional] 
**price_strategy** | **str** |  | 
**sizes** | [**List[ComboSizeDto3]**](ComboSizeDto3.md) | Available sizes for combo (can be empty) | [optional] 
**start_date** | **str** | The date when the combo will be available until | 

## Example

```python
from iikocloud_client.models.combo_dto3 import ComboDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboDto3 from a JSON string
combo_dto3_instance = ComboDto3.from_json(json)
# print the JSON string representation of the object
print(ComboDto3.to_json())

# convert the object into a dict
combo_dto3_dict = combo_dto3_instance.to_dict()
# create an instance of ComboDto3 from a dict
combo_dto3_from_dict = ComboDto3.from_dict(combo_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


