# IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest

Calculate combo price request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.md) | Items with modifiers included in combo. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


