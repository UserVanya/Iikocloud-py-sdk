# NetOrganizationMarketingCampaignActionConditionBindingInfo

Marketing campaign binding info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**stop_further_execution** | **bool** | Loyalty processing stop after successful execution of binding. So means order of bindings affects. | [optional] 
**actions** | [**List[NetOrganizationMarketingCampaignSettingsInfo]**](NetOrganizationMarketingCampaignSettingsInfo.md) | Marketing actions. | [optional] 
**conditions** | [**List[NetOrganizationMarketingCampaignSettingsInfo]**](NetOrganizationMarketingCampaignSettingsInfo.md) | Marketing conditions. | [optional] 

## Example

```python
from iikocloud_client.models.net_organization_marketing_campaign_action_condition_binding_info import NetOrganizationMarketingCampaignActionConditionBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetOrganizationMarketingCampaignActionConditionBindingInfo from a JSON string
net_organization_marketing_campaign_action_condition_binding_info_instance = NetOrganizationMarketingCampaignActionConditionBindingInfo.from_json(json)
# print the JSON string representation of the object
print(NetOrganizationMarketingCampaignActionConditionBindingInfo.to_json())

# convert the object into a dict
net_organization_marketing_campaign_action_condition_binding_info_dict = net_organization_marketing_campaign_action_condition_binding_info_instance.to_dict()
# create an instance of NetOrganizationMarketingCampaignActionConditionBindingInfo from a dict
net_organization_marketing_campaign_action_condition_binding_info_from_dict = NetOrganizationMarketingCampaignActionConditionBindingInfo.from_dict(net_organization_marketing_campaign_action_condition_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


