# IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse

Calculate combo price response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Calculated price of combo item. | [optional] 
**incorrectly_filled_groups** | **List[UUID]** | Ids of incorrectly filled groups. If not empty - price will be 0. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


