# OrganizationMarketingCampaignInfo

Marketing campaign info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Marketing campaign id. | [optional] 
**program_id** | **str** | Loyalty program id. | [optional] 
**name** | **str** | Loyalty program name. Can be null. | [optional] 
**description** | **str** | Marketing campaign description. Can be null. | [optional] 
**is_active** | **bool** | Marketing campaign is active. | [optional] 
**period_from** | **str** | Marketing campaign works since date. | [optional] 
**period_to** | **str** | Marketing campaign works till date. Null means limitless. | [optional] 
**order_action_condition_bindings** | [**List[OrganizationMarketingCampaignActionConditionBindingInfo]**](OrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked when order is processed. | [optional] 
**periodic_action_condition_bindings** | [**List[OrganizationMarketingCampaignActionConditionBindingInfo]**](OrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by schedule. | [optional] 
**overdraft_action_condition_bindings** | [**List[OrganizationMarketingCampaignActionConditionBindingInfo]**](OrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by overdraft. | [optional] 
**guest_registration_action_condition_bindings** | [**List[OrganizationMarketingCampaignActionConditionBindingInfo]**](OrganizationMarketingCampaignActionConditionBindingInfo.md) | Conditions and actions that will be checked by guest registration. | [optional] 

## Example

```python
from iikocloud_client.models.organization_marketing_campaign_info import OrganizationMarketingCampaignInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMarketingCampaignInfo from a JSON string
organization_marketing_campaign_info_instance = OrganizationMarketingCampaignInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationMarketingCampaignInfo.to_json())

# convert the object into a dict
organization_marketing_campaign_info_dict = organization_marketing_campaign_info_instance.to_dict()
# create an instance of OrganizationMarketingCampaignInfo from a dict
organization_marketing_campaign_info_from_dict = OrganizationMarketingCampaignInfo.from_dict(organization_marketing_campaign_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


