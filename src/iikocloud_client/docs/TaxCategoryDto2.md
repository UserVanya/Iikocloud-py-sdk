# TaxCategoryDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**percentage** | **float** |  | [optional] [default to 0]

## Example

```python
from iikocloud_client.models.tax_category_dto2 import TaxCategoryDto2

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategoryDto2 from a JSON string
tax_category_dto2_instance = TaxCategoryDto2.from_json(json)
# print the JSON string representation of the object
print(TaxCategoryDto2.to_json())

# convert the object into a dict
tax_category_dto2_dict = tax_category_dto2_instance.to_dict()
# create an instance of TaxCategoryDto2 from a dict
tax_category_dto2_from_dict = TaxCategoryDto2.from_dict(tax_category_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


