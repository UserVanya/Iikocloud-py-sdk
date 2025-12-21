# LoyaltyResultCalculateCheckinResponse

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_program_results** | [**List[LoyaltyResultLoyaltyProgramResult]**](LoyaltyResultLoyaltyProgramResult.md) | Loyalty program results. | [optional] 
**available_payments** | [**List[LoyaltyResultAvailablePayment]**](LoyaltyResultAvailablePayment.md) | Marketing campaigns with available payments. | [optional] 
**validation_warnings** | **List[str]** | Warnings about errors, not blocking loyalty calculation. | [optional] 
**warnings** | [**List[LoyaltyResultWarningInfo]**](LoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 
**loyalty_trace** | **str** | Loyalty trace. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_calculate_checkin_response import LoyaltyResultCalculateCheckinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCalculateCheckinResponse from a JSON string
loyalty_result_calculate_checkin_response_instance = LoyaltyResultCalculateCheckinResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCalculateCheckinResponse.to_json())

# convert the object into a dict
loyalty_result_calculate_checkin_response_dict = loyalty_result_calculate_checkin_response_instance.to_dict()
# create an instance of LoyaltyResultCalculateCheckinResponse from a dict
loyalty_result_calculate_checkin_response_from_dict = LoyaltyResultCalculateCheckinResponse.from_dict(loyalty_result_calculate_checkin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


