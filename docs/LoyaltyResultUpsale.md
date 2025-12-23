# LoyaltyResultUpsale

user tip.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **str** | Id of action that caused the suggestion. | [optional] 
**suggestion_text** | **str** | Suggestion text. | [optional] 
**description_for_user** | **str** | Description for user. | [optional] 
**product_codes** | **List[str]** | Codes of products that suggested to be added to order. | [optional] 
**products** | [**List[LoyaltyResultUpsaleProduct]**](LoyaltyResultUpsaleProduct.md) | Products that suggested to be added to order. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_upsale import LoyaltyResultUpsale

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultUpsale from a JSON string
loyalty_result_upsale_instance = LoyaltyResultUpsale.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultUpsale.to_json())

# convert the object into a dict
loyalty_result_upsale_dict = loyalty_result_upsale_instance.to_dict()
# create an instance of LoyaltyResultUpsale from a dict
loyalty_result_upsale_from_dict = LoyaltyResultUpsale.from_dict(loyalty_result_upsale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


