# CashFlowCategoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_categories** | [**List[CashFlowCategory]**](CashFlowCategory.md) | List of cash flow categories | [optional] 
**count** | **int** | Number of items returned in the response | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 

## Example

```python
from iikocloud_client.models.cash_flow_category_list_response import CashFlowCategoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryListResponse from a JSON string
cash_flow_category_list_response_instance = CashFlowCategoryListResponse.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryListResponse.to_json())

# convert the object into a dict
cash_flow_category_list_response_dict = cash_flow_category_list_response_instance.to_dict()
# create an instance of CashFlowCategoryListResponse from a dict
cash_flow_category_list_response_from_dict = CashFlowCategoryListResponse.from_dict(cash_flow_category_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


