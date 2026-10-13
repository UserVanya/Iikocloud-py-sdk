# OuterEconomicActivityNomenclatureCodeListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deleted** | **bool** | Include deleted codes in the response. Default false | [optional] 

## Example

```python
from iikocloud_client.models.outer_economic_activity_nomenclature_code_list_request import OuterEconomicActivityNomenclatureCodeListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OuterEconomicActivityNomenclatureCodeListRequest from a JSON string
outer_economic_activity_nomenclature_code_list_request_instance = OuterEconomicActivityNomenclatureCodeListRequest.from_json(json)
# print the JSON string representation of the object
print(OuterEconomicActivityNomenclatureCodeListRequest.to_json())

# convert the object into a dict
outer_economic_activity_nomenclature_code_list_request_dict = outer_economic_activity_nomenclature_code_list_request_instance.to_dict()
# create an instance of OuterEconomicActivityNomenclatureCodeListRequest from a dict
outer_economic_activity_nomenclature_code_list_request_from_dict = OuterEconomicActivityNomenclatureCodeListRequest.from_dict(outer_economic_activity_nomenclature_code_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


