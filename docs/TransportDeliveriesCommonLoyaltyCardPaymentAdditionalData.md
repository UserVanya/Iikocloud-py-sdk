# TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData

Additional data for LoyaltyApp payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | Guest credential, authorizing payment. | 
**search_scope** | [**TransportDeliveriesCommonIikoCardSearchScope**](TransportDeliveriesCommonIikoCardSearchScope.md) | Guest credential search scope. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_common_loyalty_card_payment_additional_data import TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData from a JSON string
transport_deliveries_common_loyalty_card_payment_additional_data_instance = TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData.to_json())

# convert the object into a dict
transport_deliveries_common_loyalty_card_payment_additional_data_dict = transport_deliveries_common_loyalty_card_payment_additional_data_instance.to_dict()
# create an instance of TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData from a dict
transport_deliveries_common_loyalty_card_payment_additional_data_from_dict = TransportDeliveriesCommonLoyaltyCardPaymentAdditionalData.from_dict(transport_deliveries_common_loyalty_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


