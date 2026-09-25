# TaxCategoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TaxCategory]**](TaxCategory.md) | List of tax categories | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 
**total_count** | **int** | Total number of records matching the filters | [optional] 

## Example

```python
from iikocloud_client.models.tax_category_list_response import TaxCategoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategoryListResponse from a JSON string
tax_category_list_response_instance = TaxCategoryListResponse.from_json(json)
# print the JSON string representation of the object
print(TaxCategoryListResponse.to_json())

# convert the object into a dict
tax_category_list_response_dict = tax_category_list_response_instance.to_dict()
# create an instance of TaxCategoryListResponse from a dict
tax_category_list_response_from_dict = TaxCategoryListResponse.from_dict(tax_category_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


