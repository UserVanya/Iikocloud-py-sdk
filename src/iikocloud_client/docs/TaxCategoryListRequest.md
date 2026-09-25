# TaxCategoryListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FilterCondition]**](FilterCondition.md) | Request filters. All filters are applied simultaneously (AND) | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 

## Example

```python
from iikocloud_client.models.tax_category_list_request import TaxCategoryListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategoryListRequest from a JSON string
tax_category_list_request_instance = TaxCategoryListRequest.from_json(json)
# print the JSON string representation of the object
print(TaxCategoryListRequest.to_json())

# convert the object into a dict
tax_category_list_request_dict = tax_category_list_request_instance.to_dict()
# create an instance of TaxCategoryListRequest from a dict
tax_category_list_request_from_dict = TaxCategoryListRequest.from_dict(tax_category_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


