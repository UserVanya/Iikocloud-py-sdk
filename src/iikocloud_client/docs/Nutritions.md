# Nutritions

Nutritional value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carbs** | **float** | Carbohydrates. | [optional] 
**energy** | **float** | Energy value. | [optional] 
**fats** | **float** | Fats. | [optional] 
**proteins** | **float** | Proteins. | [optional] 
**salt** | **float** | Salt. | [optional] 
**saturated_fatty_acid** | **float** | Saturated fatty acids. | [optional] 
**sugar** | **float** | Sugar. | [optional] 

## Example

```python
from iikocloud_client.models.nutritions import Nutritions

# TODO update the JSON string below
json = "{}"
# create an instance of Nutritions from a JSON string
nutritions_instance = Nutritions.from_json(json)
# print the JSON string representation of the object
print(Nutritions.to_json())

# convert the object into a dict
nutritions_dict = nutritions_instance.to_dict()
# create an instance of Nutritions from a dict
nutritions_from_dict = Nutritions.from_dict(nutritions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


