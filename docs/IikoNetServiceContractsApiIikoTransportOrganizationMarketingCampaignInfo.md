# IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo

Marketing campaign info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Marketing campaign id. | [optional] 
**program_id** | **UUID** | Loyalty program id. | [optional] 
**name** | **str** | Loyalty program name. Can be null. | [optional] 
**description** | **str** | Marketing campaign description. Can be null. | [optional] 
**is_active** | **bool** | Marketing campaign is active. | [optional] 
**period_from** | **str** | Marketing campaign works since date. | [optional] 
**period_to** | **str** | Marketing campaign works till date. Null means limitless. | [optional] 
**order_action_condition_bindings** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked when order is processed. | [optional] 
**periodic_action_condition_bindings** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by schedule. | [optional] 
**overdraft_action_condition_bindings** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by overdraft. | [optional] 
**guest_registration_action_condition_bindings** | [**List[IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo]**](IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by guest registration. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info import IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info_instance = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info_dict = iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo from a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info_from_dict = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


