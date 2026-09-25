# CashFlowCategoryListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[CashFlowCategoriesFilter]**](CashFlowCategoriesFilter.md) | Request filters. All filters are applied simultaneously (AND) | 
**limit** | **int** | Maximum number of records in the response. | 
**offset** | **int** | Number of records to skip from the beginning. | 

## Example

```python
from iikocloud_client.models.cash_flow_category_list_request import CashFlowCategoryListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryListRequest from a JSON string
cash_flow_category_list_request_instance = CashFlowCategoryListRequest.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryListRequest.to_json())

# convert the object into a dict
cash_flow_category_list_request_dict = cash_flow_category_list_request_instance.to_dict()
# create an instance of CashFlowCategoryListRequest from a dict
cash_flow_category_list_request_from_dict = CashFlowCategoryListRequest.from_dict(cash_flow_category_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


