# IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup

Information about combos group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**name** | **str** | Name. | [optional] 
**is_main_group** | **bool** | Is main group. | [optional] 
**products** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboProduct.md) | Products. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group import IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


