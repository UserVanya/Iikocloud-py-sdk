# LoyaltyResultGetManualConditionsResponse

Get manual conditions response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_conditions** | [**List[LoyaltyResultManualConditionInfo]**](LoyaltyResultManualConditionInfo.md) | Info about manual conditions. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_get_manual_conditions_response import LoyaltyResultGetManualConditionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGetManualConditionsResponse from a JSON string
loyalty_result_get_manual_conditions_response_instance = LoyaltyResultGetManualConditionsResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGetManualConditionsResponse.to_json())

# convert the object into a dict
loyalty_result_get_manual_conditions_response_dict = loyalty_result_get_manual_conditions_response_instance.to_dict()
# create an instance of LoyaltyResultGetManualConditionsResponse from a dict
loyalty_result_get_manual_conditions_response_from_dict = LoyaltyResultGetManualConditionsResponse.from_dict(loyalty_result_get_manual_conditions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


