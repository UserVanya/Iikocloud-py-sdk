# NetOrganizationLoyaltyProgram

Loyalty program.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Program id. | [optional] 
**name** | **str** | Program name. Can be null. | [optional] 
**description** | **str** | Program description. Can be null. | [optional] 
**service_from** | **str** | Program works since date. | [optional] 
**service_to** | **str** | Program works till date. | [optional] 
**notify_about_balance_changes** | **bool** | Notify customer when balance has changed (sms/push). | [optional] 
**program_type** | [**NetProgramType**](NetProgramType.md) | Program type.  &lt;br&gt;0 - deposit or corporate nutrition,&lt;br /&gt;1 - bonus program,&lt;br /&gt;2 - products program,&lt;br /&gt;3 - discount program,&lt;br /&gt;4 - certificate program. | [optional] 
**is_active** | **bool** | Program is active. | [optional] 
**wallet_id** | **str** | Wallet id. Program has only wallet that means global payment type for customers. | [optional] 
**marketing_campaigns** | [**List[NetOrganizationMarketingCampaignInfo]**](NetOrganizationMarketingCampaignInfo.md) | Program marketing campaigns. | [optional] 
**applied_organizations** | **List[str]** | Program applied organizations. | [optional] 
**template_type** | [**IikoNetCommonEnumsTemplateType**](IikoNetCommonEnumsTemplateType.md) | Program template type.  &lt;br&gt;0 - None,&lt;br /&gt;1 - BonusProgram,&lt;br /&gt;2 - DiscountProgram,&lt;br /&gt;3 - NthDishProgram,&lt;br /&gt;4 - ManualOrderAnonymousDiscount,&lt;br /&gt;5 - AutoOrderAnonymousDiscount,&lt;br /&gt;6 - AutoDishAnonymousDiscount,&lt;br /&gt;7 - PromotionsProgram,&lt;br /&gt;8 - NthDishPromotionsProgram. | [optional] 
**is_exchange_rate_enabled** | **bool** | Exchange rate for bonuses and real currency. | [optional] 
**refill_type** | [**IikoNetCommonEnumsRefillType**](IikoNetCommonEnumsRefillType.md) | Refill type with payment. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_organization_loyalty_program import NetOrganizationLoyaltyProgram

# TODO update the JSON string below
json = "{}"
# create an instance of NetOrganizationLoyaltyProgram from a JSON string
net_organization_loyalty_program_instance = NetOrganizationLoyaltyProgram.from_json(json)
# print the JSON string representation of the object
print(NetOrganizationLoyaltyProgram.to_json())

# convert the object into a dict
net_organization_loyalty_program_dict = net_organization_loyalty_program_instance.to_dict()
# create an instance of NetOrganizationLoyaltyProgram from a dict
net_organization_loyalty_program_from_dict = NetOrganizationLoyaltyProgram.from_dict(net_organization_loyalty_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


