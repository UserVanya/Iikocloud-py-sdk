# NutritionInfoDto4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fats** | **float** | Fats | [optional] [default to 0]
**proteins** | **float** | Proteins | [optional] [default to 0]
**carbs** | **float** | Carbohydrate | [optional] [default to 0]
**energy** | **float** | Calories | [optional] [default to 0]
**organizations** | **List[str]** | List of organization GUIDs | [optional] 
**saturated_fatty_acid** | **float** | Saturated Fatty Acid | [optional] 
**salt** | **float** | Salt | [optional] 
**sugar** | **float** | Sugar | [optional] 

## Example

```python
from iikocloud_client.models.nutrition_info_dto4 import NutritionInfoDto4

# TODO update the JSON string below
json = "{}"
# create an instance of NutritionInfoDto4 from a JSON string
nutrition_info_dto4_instance = NutritionInfoDto4.from_json(json)
# print the JSON string representation of the object
print(NutritionInfoDto4.to_json())

# convert the object into a dict
nutrition_info_dto4_dict = nutrition_info_dto4_instance.to_dict()
# create an instance of NutritionInfoDto4 from a dict
nutrition_info_dto4_from_dict = NutritionInfoDto4.from_dict(nutrition_info_dto4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


