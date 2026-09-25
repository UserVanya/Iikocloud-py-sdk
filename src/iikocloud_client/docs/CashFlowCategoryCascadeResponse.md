# CashFlowCategoryCascadeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_ids** | **List[str]** | List of affected cash flow category identifiers | [optional] 
**id** | **str** | Cash flow category UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 

## Example

```python
from iikocloud_client.models.cash_flow_category_cascade_response import CashFlowCategoryCascadeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCategoryCascadeResponse from a JSON string
cash_flow_category_cascade_response_instance = CashFlowCategoryCascadeResponse.from_json(json)
# print the JSON string representation of the object
print(CashFlowCategoryCascadeResponse.to_json())

# convert the object into a dict
cash_flow_category_cascade_response_dict = cash_flow_category_cascade_response_instance.to_dict()
# create an instance of CashFlowCategoryCascadeResponse from a dict
cash_flow_category_cascade_response_from_dict = CashFlowCategoryCascadeResponse.from_dict(cash_flow_category_cascade_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


