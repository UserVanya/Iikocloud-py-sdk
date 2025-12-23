# LoyaltyResultCalculateComboPriceResponse

Calculate combo price response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Calculated price of combo item. | [optional] 
**incorrectly_filled_groups** | **List[str]** | Ids of incorrectly filled groups. If not empty - price will be 0. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_calculate_combo_price_response import LoyaltyResultCalculateComboPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCalculateComboPriceResponse from a JSON string
loyalty_result_calculate_combo_price_response_instance = LoyaltyResultCalculateComboPriceResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCalculateComboPriceResponse.to_json())

# convert the object into a dict
loyalty_result_calculate_combo_price_response_dict = loyalty_result_calculate_combo_price_response_instance.to_dict()
# create an instance of LoyaltyResultCalculateComboPriceResponse from a dict
loyalty_result_calculate_combo_price_response_from_dict = LoyaltyResultCalculateComboPriceResponse.from_dict(loyalty_result_calculate_combo_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


