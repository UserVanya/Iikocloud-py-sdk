# IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo

Marketing campaign settings info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**settings** | **str** | Action/condition settings. Stored as Json. Can be null. | [optional] 
**type_name** | **str** | Action/condition type name. Can be null. | [optional] 
**check_sum** | **str** | Hash value of checksum. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info import IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info_instance = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info_dict = iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo from a dict
iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info_from_dict = IikoNetServiceContractsApiIikoTransportOrganizationMarketingCampaignSettingsInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_organization_marketing_campaign_settings_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


