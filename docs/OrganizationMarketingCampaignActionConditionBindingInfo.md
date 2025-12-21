# OrganizationMarketingCampaignActionConditionBindingInfo

Marketing campaign binding info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**stop_further_execution** | **bool** | Loyalty processing stop after successful execution of binding. So means order of bindings affects. | [optional] 
**actions** | [**List[OrganizationMarketingCampaignSettingsInfo]**](OrganizationMarketingCampaignSettingsInfo.md) | Marketing actions. | [optional] 
**conditions** | [**List[OrganizationMarketingCampaignSettingsInfo]**](OrganizationMarketingCampaignSettingsInfo.md) | Marketing conditions. | [optional] 

## Example

```python
from iikocloud_client.models.organization_marketing_campaign_action_condition_binding_info import OrganizationMarketingCampaignActionConditionBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMarketingCampaignActionConditionBindingInfo from a JSON string
organization_marketing_campaign_action_condition_binding_info_instance = OrganizationMarketingCampaignActionConditionBindingInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationMarketingCampaignActionConditionBindingInfo.to_json())

# convert the object into a dict
organization_marketing_campaign_action_condition_binding_info_dict = organization_marketing_campaign_action_condition_binding_info_instance.to_dict()
# create an instance of OrganizationMarketingCampaignActionConditionBindingInfo from a dict
organization_marketing_campaign_action_condition_binding_info_from_dict = OrganizationMarketingCampaignActionConditionBindingInfo.from_dict(organization_marketing_campaign_action_condition_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


