# IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo

Available combo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_id** | **UUID** | Id of combo specification, describing combo content. | [optional] 
**group_mapping** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroupMapping]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroupMapping.md) | Groups contained in combo. If null - there is no suitable product in order yet for that group. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo import IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_available_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


