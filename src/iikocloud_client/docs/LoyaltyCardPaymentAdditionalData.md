# LoyaltyCardPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | Guest credential, authorizing payment. | 
**search_scope** | [**IikoCardSearchScope**](IikoCardSearchScope.md) | Guest credential search scope. | 

## Example

```python
from iikocloud_client.models.loyalty_card_payment_additional_data import LoyaltyCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyCardPaymentAdditionalData from a JSON string
loyalty_card_payment_additional_data_instance = LoyaltyCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(LoyaltyCardPaymentAdditionalData.to_json())

# convert the object into a dict
loyalty_card_payment_additional_data_dict = loyalty_card_payment_additional_data_instance.to_dict()
# create an instance of LoyaltyCardPaymentAdditionalData from a dict
loyalty_card_payment_additional_data_from_dict = LoyaltyCardPaymentAdditionalData.from_dict(loyalty_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


