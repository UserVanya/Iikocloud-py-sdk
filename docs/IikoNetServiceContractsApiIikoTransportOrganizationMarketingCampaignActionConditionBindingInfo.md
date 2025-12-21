# IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo

Marketing campaign binding info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**stop_further_execution** | **bool** | Loyalty processing stop after successful execution of binding. So means order of bindings affects. | [optional] 
**actions** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo.md) | Marketing actions. | [optional] 
**conditions** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo.md) | Marketing conditions. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info import IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info_instance = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info_dict = iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo from a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info_from_dict = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_action_condition_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


