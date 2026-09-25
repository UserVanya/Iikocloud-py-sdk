# AccountingCategoryGetByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier (UUID) | [optional] 

## Example

```python
from iikocloud_client.models.accounting_category_get_by_id_request import AccountingCategoryGetByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingCategoryGetByIDRequest from a JSON string
accounting_category_get_by_id_request_instance = AccountingCategoryGetByIDRequest.from_json(json)
# print the JSON string representation of the object
print(AccountingCategoryGetByIDRequest.to_json())

# convert the object into a dict
accounting_category_get_by_id_request_dict = accounting_category_get_by_id_request_instance.to_dict()
# create an instance of AccountingCategoryGetByIDRequest from a dict
accounting_category_get_by_id_request_from_dict = AccountingCategoryGetByIDRequest.from_dict(accounting_category_get_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


