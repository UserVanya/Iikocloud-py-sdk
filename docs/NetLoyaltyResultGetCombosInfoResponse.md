# NetLoyaltyResultGetCombosInfoResponse

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_specifications** | [**List[NetLoyaltyResultComboSpecification]**](NetLoyaltyResultComboSpecification.md) | Full combo&#39;s specifications. | [optional] 
**combo_categories** | [**List[NetLoyaltyResultComboCategory]**](NetLoyaltyResultComboCategory.md) | Combo&#39;s categories. | [optional] 
**warnings** | [**List[NetLoyaltyResultWarningInfo]**](NetLoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_get_combos_info_response import NetLoyaltyResultGetCombosInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGetCombosInfoResponse from a JSON string
net_loyalty_result_get_combos_info_response_instance = NetLoyaltyResultGetCombosInfoResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGetCombosInfoResponse.to_json())

# convert the object into a dict
net_loyalty_result_get_combos_info_response_dict = net_loyalty_result_get_combos_info_response_instance.to_dict()
# create an instance of NetLoyaltyResultGetCombosInfoResponse from a dict
net_loyalty_result_get_combos_info_response_from_dict = NetLoyaltyResultGetCombosInfoResponse.from_dict(net_loyalty_result_get_combos_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


