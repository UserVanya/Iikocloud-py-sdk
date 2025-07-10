# NetLoyaltyResultCalculateComboPriceResponse

Calculate combo price response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Calculated price of combo item. | [optional] 
**incorrectly_filled_groups** | **List[str]** | Ids of incorrectly filled groups. If not empty - price will be 0. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_calculate_combo_price_response import NetLoyaltyResultCalculateComboPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCalculateComboPriceResponse from a JSON string
net_loyalty_result_calculate_combo_price_response_instance = NetLoyaltyResultCalculateComboPriceResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCalculateComboPriceResponse.to_json())

# convert the object into a dict
net_loyalty_result_calculate_combo_price_response_dict = net_loyalty_result_calculate_combo_price_response_instance.to_dict()
# create an instance of NetLoyaltyResultCalculateComboPriceResponse from a dict
net_loyalty_result_calculate_combo_price_response_from_dict = NetLoyaltyResultCalculateComboPriceResponse.from_dict(net_loyalty_result_calculate_combo_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


