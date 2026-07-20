# MarketingCampaignInfo

Marketing campaign info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Marketing campaign description. Can be null. | [optional] 
**guest_registration_action_condition_bindings** | [**List[MarketingCampaignActionConditionBindingInfo]**](MarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by guest registration. | [optional] 
**id** | **UUID** | Marketing campaign id. | [optional] 
**is_active** | **bool** | Marketing campaign is active. | [optional] 
**name** | **str** | Loyalty program name. Can be null. | [optional] 
**order_action_condition_bindings** | [**List[MarketingCampaignActionConditionBindingInfo]**](MarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked when order is processed. | [optional] 
**overdraft_action_condition_bindings** | [**List[MarketingCampaignActionConditionBindingInfo]**](MarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by overdraft. | [optional] 
**period_from** | **str** | Marketing campaign works since date. | [optional] 
**period_to** | **str** | Marketing campaign works till date. Null means limitless. | [optional] 
**periodic_action_condition_bindings** | [**List[MarketingCampaignActionConditionBindingInfo]**](MarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by schedule. | [optional] 
**program_id** | **UUID** | Loyalty program id. | [optional] 

## Example

```python
from iikocloud_client.models.marketing_campaign_info import MarketingCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCampaignInfo from a JSON string
marketing_campaign_info_instance = MarketingCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(MarketingCampaignInfo.to_json())

# convert the object into a dict
marketing_campaign_info_dict = marketing_campaign_info_instance.to_dict()
# create an instance of MarketingCampaignInfo from a dict
marketing_campaign_info_from_dict = MarketingCampaignInfo.from_dict(marketing_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


