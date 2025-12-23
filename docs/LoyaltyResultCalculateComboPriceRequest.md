# LoyaltyResultCalculateComboPriceRequest

Calculate combo price request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Items with modifiers included in combo. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.loyalty_result_calculate_combo_price_request import LoyaltyResultCalculateComboPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCalculateComboPriceRequest from a JSON string
loyalty_result_calculate_combo_price_request_instance = LoyaltyResultCalculateComboPriceRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCalculateComboPriceRequest.to_json())

# convert the object into a dict
loyalty_result_calculate_combo_price_request_dict = loyalty_result_calculate_combo_price_request_instance.to_dict()
# create an instance of LoyaltyResultCalculateComboPriceRequest from a dict
loyalty_result_calculate_combo_price_request_from_dict = LoyaltyResultCalculateComboPriceRequest.from_dict(loyalty_result_calculate_combo_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


