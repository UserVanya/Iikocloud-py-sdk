# NetLoyaltyResultCalculateCheckinResponse

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_program_results** | [**List[NetLoyaltyResultLoyaltyProgramResult]**](NetLoyaltyResultLoyaltyProgramResult.md) | Loyalty program results. | [optional] 
**available_payments** | [**List[NetLoyaltyResultAvailablePayment]**](NetLoyaltyResultAvailablePayment.md) | Marketing campaigns with available payments. | [optional] 
**validation_warnings** | **List[str]** | Warnings about errors, not blocking loyalty calculation. | [optional] 
**warnings** | [**List[NetLoyaltyResultWarningInfo]**](NetLoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 
**loyalty_trace** | **str** | Loyalty trace. Can be null. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_calculate_checkin_response import NetLoyaltyResultCalculateCheckinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCalculateCheckinResponse from a JSON string
net_loyalty_result_calculate_checkin_response_instance = NetLoyaltyResultCalculateCheckinResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCalculateCheckinResponse.to_json())

# convert the object into a dict
net_loyalty_result_calculate_checkin_response_dict = net_loyalty_result_calculate_checkin_response_instance.to_dict()
# create an instance of NetLoyaltyResultCalculateCheckinResponse from a dict
net_loyalty_result_calculate_checkin_response_from_dict = NetLoyaltyResultCalculateCheckinResponse.from_dict(net_loyalty_result_calculate_checkin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


