# AccountingCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User-defined accounting category code | [optional] 
**id** | **str** | Accounting category identifier (UUID) | [optional] 
**is_deleted** | **bool** | Flag indicating that the accounting category is logically deleted | [optional] 
**name** | **str** | Display name of the accounting category | [optional] 

## Example

```python
from iikocloud_client.models.accounting_category import AccountingCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingCategory from a JSON string
accounting_category_instance = AccountingCategory.from_json(json)
# print the JSON string representation of the object
print(AccountingCategory.to_json())

# convert the object into a dict
accounting_category_dict = accounting_category_instance.to_dict()
# create an instance of AccountingCategory from a dict
accounting_category_from_dict = AccountingCategory.from_dict(accounting_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


