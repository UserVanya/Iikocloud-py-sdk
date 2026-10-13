# OuterEconomicActivityNomenclatureCodeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OuterEconomicActivityNomenclatureCode]**](OuterEconomicActivityNomenclatureCode.md) | List of foreign economic activity commodity codes | [optional] 
**total_count** | **int** | Total number of foreign economic activity commodity codes matching the request | [optional] 

## Example

```python
from iikocloud_client.models.outer_economic_activity_nomenclature_code_list_response import OuterEconomicActivityNomenclatureCodeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OuterEconomicActivityNomenclatureCodeListResponse from a JSON string
outer_economic_activity_nomenclature_code_list_response_instance = OuterEconomicActivityNomenclatureCodeListResponse.from_json(json)
# print the JSON string representation of the object
print(OuterEconomicActivityNomenclatureCodeListResponse.to_json())

# convert the object into a dict
outer_economic_activity_nomenclature_code_list_response_dict = outer_economic_activity_nomenclature_code_list_response_instance.to_dict()
# create an instance of OuterEconomicActivityNomenclatureCodeListResponse from a dict
outer_economic_activity_nomenclature_code_list_response_from_dict = OuterEconomicActivityNomenclatureCodeListResponse.from_dict(outer_economic_activity_nomenclature_code_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


