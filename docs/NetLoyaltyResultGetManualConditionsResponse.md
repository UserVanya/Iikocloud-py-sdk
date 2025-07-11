# NetLoyaltyResultGetManualConditionsResponse

Get manual conditions response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_conditions** | [**List[NetLoyaltyResultManualConditionInfo]**](NetLoyaltyResultManualConditionInfo.md) | Info about manual conditions. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_get_manual_conditions_response import NetLoyaltyResultGetManualConditionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGetManualConditionsResponse from a JSON string
net_loyalty_result_get_manual_conditions_response_instance = NetLoyaltyResultGetManualConditionsResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGetManualConditionsResponse.to_json())

# convert the object into a dict
net_loyalty_result_get_manual_conditions_response_dict = net_loyalty_result_get_manual_conditions_response_instance.to_dict()
# create an instance of NetLoyaltyResultGetManualConditionsResponse from a dict
net_loyalty_result_get_manual_conditions_response_from_dict = NetLoyaltyResultGetManualConditionsResponse.from_dict(net_loyalty_result_get_manual_conditions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


