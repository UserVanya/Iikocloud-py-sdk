# OrganizationMarketingCampaignSettingsInfo

Marketing campaign settings info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**settings** | **str** | Action/condition settings. Stored as Json. Can be null. | [optional] 
**type_name** | **str** | Action/condition type name. Can be null. | [optional] 
**check_sum** | **str** | Hash value of checksum. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.organization_marketing_campaign_settings_info import OrganizationMarketingCampaignSettingsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMarketingCampaignSettingsInfo from a JSON string
organization_marketing_campaign_settings_info_instance = OrganizationMarketingCampaignSettingsInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationMarketingCampaignSettingsInfo.to_json())

# convert the object into a dict
organization_marketing_campaign_settings_info_dict = organization_marketing_campaign_settings_info_instance.to_dict()
# create an instance of OrganizationMarketingCampaignSettingsInfo from a dict
organization_marketing_campaign_settings_info_from_dict = OrganizationMarketingCampaignSettingsInfo.from_dict(organization_marketing_campaign_settings_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


