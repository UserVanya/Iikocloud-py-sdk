# NutritionInfoDto6


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
from iikocloud_client.models.nutrition_info_dto6 import NutritionInfoDto6

# TODO update the JSON string below
json = "{}"
# create an instance of NutritionInfoDto6 from a JSON string
nutrition_info_dto6_instance = NutritionInfoDto6.from_json(json)
# print the JSON string representation of the object
print(NutritionInfoDto6.to_json())

# convert the object into a dict
nutrition_info_dto6_dict = nutrition_info_dto6_instance.to_dict()
# create an instance of NutritionInfoDto6 from a dict
nutrition_info_dto6_from_dict = NutritionInfoDto6.from_dict(nutrition_info_dto6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


