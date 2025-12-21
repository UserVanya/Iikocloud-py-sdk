# IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** | Guest credential, authorizing payment. | 
**search_scope** | [**IikoTransportPublicApiContractsDeliveriesCommonIikoCardSearchScope**](IikoTransportPublicApiContractsDeliveriesCommonIikoCardSearchScope.md) | Guest credential search scope. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data import IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData from a JSON string
iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data_instance = IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data_dict = iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData from a dict
iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data_from_dict = IikoTransportPublicApiContractsDeliveriesCommonLoyaltyCardPaymentAdditionalData.from_dict(iiko_transport_public_api_contracts_deliveries_common_loyalty_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


