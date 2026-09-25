# CashRegisterListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CashRegisterListItem]**](CashRegisterListItem.md) | Cash registers | [optional] 
**limit** | **int** | Items per page. Default value: &#x60;50&#x60;, from &#x60;1&#x60; to &#x60;1000&#x60; | [optional] 
**offset** | **int** | Offset. Default value: &#x60;0&#x60;, non-negative | [optional] 
**total_count** | **int** | Total number of matches before pagination | [optional] 

## Example

```python
from iikocloud_client.models.cash_register_list_response import CashRegisterListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CashRegisterListResponse from a JSON string
cash_register_list_response_instance = CashRegisterListResponse.from_json(json)
# print the JSON string representation of the object
print(CashRegisterListResponse.to_json())

# convert the object into a dict
cash_register_list_response_dict = cash_register_list_response_instance.to_dict()
# create an instance of CashRegisterListResponse from a dict
cash_register_list_response_from_dict = CashRegisterListResponse.from_dict(cash_register_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


