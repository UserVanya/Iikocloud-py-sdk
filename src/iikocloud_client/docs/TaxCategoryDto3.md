# TaxCategoryDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**percentage** | **float** |  | [optional] [default to 0]

## Example

```python
from iikocloud_client.models.tax_category_dto3 import TaxCategoryDto3

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategoryDto3 from a JSON string
tax_category_dto3_instance = TaxCategoryDto3.from_json(json)
# print the JSON string representation of the object
print(TaxCategoryDto3.to_json())

# convert the object into a dict
tax_category_dto3_dict = tax_category_dto3_instance.to_dict()
# create an instance of TaxCategoryDto3 from a dict
tax_category_dto3_from_dict = TaxCategoryDto3.from_dict(tax_category_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


