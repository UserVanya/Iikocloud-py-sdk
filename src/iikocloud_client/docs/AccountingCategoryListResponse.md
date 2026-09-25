# AccountingCategoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[AccountingCategory]**](AccountingCategory.md) | List of entities | [optional] 
**limit** | **int** | Limit value from the request | [optional] 
**offset** | **int** | Offset value from the request | [optional] 
**total_count** | **int** | Total number of records matching the filter | [optional] 

## Example

```python
from iikocloud_client.models.accounting_category_list_response import AccountingCategoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingCategoryListResponse from a JSON string
accounting_category_list_response_instance = AccountingCategoryListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountingCategoryListResponse.to_json())

# convert the object into a dict
accounting_category_list_response_dict = accounting_category_list_response_instance.to_dict()
# create an instance of AccountingCategoryListResponse from a dict
accounting_category_list_response_from_dict = AccountingCategoryListResponse.from_dict(accounting_category_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


