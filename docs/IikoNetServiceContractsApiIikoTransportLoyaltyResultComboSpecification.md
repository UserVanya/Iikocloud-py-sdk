# IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **UUID** | Id of action that added the combo. | [optional] 
**category_id** | **UUID** | Combo&#39;s category id. | [optional] 
**name** | **str** | Name. Can be null. | [optional] 
**price_modification_type** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultComboPriceModificationType**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboPriceModificationType.md) | Price modification type.  &lt;br&gt;0 - fixed combo price,&lt;br /&gt;1 - fixed position price,&lt;br /&gt;2 - cheapest position discount,&lt;br /&gt;3 - most expensive position discount,&lt;br /&gt;4 - percentage discount for each position. | [optional] 
**price_modification** | **float** | Price modification. | [optional] 
**is_active** | **bool** | Is active. | [optional] 
**start_date** | **str** | Start date. | [optional] 
**expiration_date** | **str** | Expiration date. | [optional] 
**lacking_groups_to_suggest** | **int** | Lacking groups to suggest. | [optional] 
**include_modifiers** | **bool** | Include modifiers. | [optional] 
**groups** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboGroup.md) | Groups. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification import IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_combo_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


