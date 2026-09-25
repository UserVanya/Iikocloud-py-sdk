# AccountingCategoryListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | Filter by deletion status; omit to return all records | [optional] 
**limit** | **int** | Maximum number of records (0 &#x3D; no limit) | [optional] 
**offset** | **int** | Number of records to skip | [optional] 
**revision** | **int** | Return only records with revision &gt;&#x3D; this value | [optional] 

## Example

```python
from iikocloud_client.models.accounting_category_list_request import AccountingCategoryListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingCategoryListRequest from a JSON string
accounting_category_list_request_instance = AccountingCategoryListRequest.from_json(json)
# print the JSON string representation of the object
print(AccountingCategoryListRequest.to_json())

# convert the object into a dict
accounting_category_list_request_dict = accounting_category_list_request_instance.to_dict()
# create an instance of AccountingCategoryListRequest from a dict
accounting_category_list_request_from_dict = AccountingCategoryListRequest.from_dict(accounting_category_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


