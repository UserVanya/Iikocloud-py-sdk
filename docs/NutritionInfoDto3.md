# NutritionInfoDto3


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
from iikocloud_client.models.nutrition_info_dto3 import NutritionInfoDto3

# TODO update the JSON string below
json = "{}"
# create an instance of NutritionInfoDto3 from a JSON string
nutrition_info_dto3_instance = NutritionInfoDto3.from_json(json)
# print the JSON string representation of the object
print(NutritionInfoDto3.to_json())

# convert the object into a dict
nutrition_info_dto3_dict = nutrition_info_dto3_instance.to_dict()
# create an instance of NutritionInfoDto3 from a dict
nutrition_info_dto3_from_dict = NutritionInfoDto3.from_dict(nutrition_info_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


