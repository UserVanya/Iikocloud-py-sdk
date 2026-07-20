# MarketingCampaignActionConditionBindingInfo

Marketing campaign binding info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[MarketingCampaignSettingsInfo]**](MarketingCampaignSettingsInfo.md) | Marketing actions. | [optional] 
**conditions** | [**List[MarketingCampaignSettingsInfo]**](MarketingCampaignSettingsInfo.md) | Marketing conditions. | [optional] 
**id** | **UUID** | Id. | [optional] 
**stop_further_execution** | **bool** | Loyalty processing stop after successful execution of binding. So means order of bindings affects. | [optional] 

## Example

```python
from iikocloud_client.models.marketing_campaign_action_condition_binding_info import MarketingCampaignActionConditionBindingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCampaignActionConditionBindingInfo from a JSON string
marketing_campaign_action_condition_binding_info_instance = MarketingCampaignActionConditionBindingInfo.from_json(json)
# print the JSON string representation of the object
print(MarketingCampaignActionConditionBindingInfo.to_json())

# convert the object into a dict
marketing_campaign_action_condition_binding_info_dict = marketing_campaign_action_condition_binding_info_instance.to_dict()
# create an instance of MarketingCampaignActionConditionBindingInfo from a dict
marketing_campaign_action_condition_binding_info_from_dict = MarketingCampaignActionConditionBindingInfo.from_dict(marketing_campaign_action_condition_binding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


