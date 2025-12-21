# LoyaltyResultGetCombosInfoResponse

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_specifications** | [**List[LoyaltyResultComboSpecification]**](LoyaltyResultComboSpecification.md) | Full combo&#39;s specifications. | [optional] 
**combo_categories** | [**List[LoyaltyResultComboCategory]**](LoyaltyResultComboCategory.md) | Combo&#39;s categories. | [optional] 
**warnings** | [**List[LoyaltyResultWarningInfo]**](LoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_get_combos_info_response import LoyaltyResultGetCombosInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGetCombosInfoResponse from a JSON string
loyalty_result_get_combos_info_response_instance = LoyaltyResultGetCombosInfoResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGetCombosInfoResponse.to_json())

# convert the object into a dict
loyalty_result_get_combos_info_response_dict = loyalty_result_get_combos_info_response_instance.to_dict()
# create an instance of LoyaltyResultGetCombosInfoResponse from a dict
loyalty_result_get_combos_info_response_from_dict = LoyaltyResultGetCombosInfoResponse.from_dict(loyalty_result_get_combos_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


