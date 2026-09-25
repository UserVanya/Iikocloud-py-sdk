# FinanceAccountsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter by | [optional] 
**op** | **str** | Comparison operator: \&quot;eq\&quot; (equal), \&quot;ne\&quot; (not equal), \&quot;gt\&quot; (greater than), \&quot;gte\&quot; (greater than or equal), \&quot;lt\&quot; (less than), \&quot;lte\&quot; (less than or equal), \&quot;in\&quot; (value is in the list - uses values[]), \&quot;nin\&quot; (value is not in the list - uses values[]), \&quot;like\&quot; (substring search, case-insensitive), \&quot;blank\&quot; (null or empty string), \&quot;notblank\&quot; (neither null nor empty string) | [optional] 
**value** | **object** | Scalar value for filtering (used with eq, ne, gt, gte, lt, lte, like) | [optional] 
**values** | **List[str]** | Array of values for multiple filtering (used with \&quot;in\&quot;, \&quot;nin\&quot;) | [optional] 

## Example

```python
from iikocloud_client.models.finance_accounts_filter import FinanceAccountsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FinanceAccountsFilter from a JSON string
finance_accounts_filter_instance = FinanceAccountsFilter.from_json(json)
# print the JSON string representation of the object
print(FinanceAccountsFilter.to_json())

# convert the object into a dict
finance_accounts_filter_dict = finance_accounts_filter_instance.to_dict()
# create an instance of FinanceAccountsFilter from a dict
finance_accounts_filter_from_dict = FinanceAccountsFilter.from_dict(finance_accounts_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


