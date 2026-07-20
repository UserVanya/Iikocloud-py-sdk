# TaxCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**percentage** | **float** |  | [optional] [default to 0]

## Example

```python
from iikocloud_client.models.tax_category_dto import TaxCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategoryDto from a JSON string
tax_category_dto_instance = TaxCategoryDto.from_json(json)
# print the JSON string representation of the object
print(TaxCategoryDto.to_json())

# convert the object into a dict
tax_category_dto_dict = tax_category_dto_instance.to_dict()
# create an instance of TaxCategoryDto from a dict
tax_category_dto_from_dict = TaxCategoryDto.from_dict(tax_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


