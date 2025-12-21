# DeliveriesCommonLoyaltyCardPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | Guest credential, authorizing payment. | 
**search_scope** | [**DeliveriesCommonIikoCardSearchScope**](DeliveriesCommonIikoCardSearchScope.md) | Guest credential search scope. | 

## Example

```python
from iikocloud_client.models.deliveries_common_loyalty_card_payment_additional_data import DeliveriesCommonLoyaltyCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonLoyaltyCardPaymentAdditionalData from a JSON string
deliveries_common_loyalty_card_payment_additional_data_instance = DeliveriesCommonLoyaltyCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonLoyaltyCardPaymentAdditionalData.to_json())

# convert the object into a dict
deliveries_common_loyalty_card_payment_additional_data_dict = deliveries_common_loyalty_card_payment_additional_data_instance.to_dict()
# create an instance of DeliveriesCommonLoyaltyCardPaymentAdditionalData from a dict
deliveries_common_loyalty_card_payment_additional_data_from_dict = DeliveriesCommonLoyaltyCardPaymentAdditionalData.from_dict(deliveries_common_loyalty_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


