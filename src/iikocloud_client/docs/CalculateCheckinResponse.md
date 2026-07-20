# CalculateCheckinResponse

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**List[WarningInfo]**](WarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 
**available_payments** | [**List[AvailablePayment]**](AvailablePayment.md) | Marketing campaigns with available payments. | [optional] 
**loyalty_program_results** | [**List[LoyaltyProgramResult]**](LoyaltyProgramResult.md) | Loyalty program results. | [optional] 
**loyalty_trace** | **str** | Loyalty trace. Can be null. | [optional] 
**validation_warnings** | **List[str]** | Warnings about errors, not blocking loyalty calculation. | [optional] 

## Example

```python
from iikocloud_client.models.calculate_checkin_response import CalculateCheckinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateCheckinResponse from a JSON string
calculate_checkin_response_instance = CalculateCheckinResponse.from_json(json)
# print the JSON string representation of the object
print(CalculateCheckinResponse.to_json())

# convert the object into a dict
calculate_checkin_response_dict = calculate_checkin_response_instance.to_dict()
# create an instance of CalculateCheckinResponse from a dict
calculate_checkin_response_from_dict = CalculateCheckinResponse.from_dict(calculate_checkin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


