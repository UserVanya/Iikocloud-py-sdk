# CashFlowCategoryGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cash flow category UUID. string (UUID) | 

## Example

```python
from iikocloud_client.models.cash_flow_category_get_request import CashFlowCategoryGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryGetRequest from a JSON string
cash_flow_category_get_request_instance = CashFlowCategoryGetRequest.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryGetRequest.to_json())

# convert the object into a dict
cash_flow_category_get_request_dict = cash_flow_category_get_request_instance.to_dict()
# create an instance of CashFlowCategoryGetRequest from a dict
cash_flow_category_get_request_from_dict = CashFlowCategoryGetRequest.from_dict(cash_flow_category_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


