# MarketingCampaignSettingsInfo

Marketing campaign settings info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_sum** | **str** | Hash value of checksum. Can be null. | [optional] 
**id** | **UUID** | Id. | [optional] 
**settings** | **str** | Action/condition settings. Stored as Json. Can be null. | [optional] 
**type_name** | **str** | Action/condition type name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.marketing_campaign_settings_info import MarketingCampaignSettingsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCampaignSettingsInfo from a JSON string
marketing_campaign_settings_info_instance = MarketingCampaignSettingsInfo.from_json(json)
# print the JSON string representation of the object
print(MarketingCampaignSettingsInfo.to_json())

# convert the object into a dict
marketing_campaign_settings_info_dict = marketing_campaign_settings_info_instance.to_dict()
# create an instance of MarketingCampaignSettingsInfo from a dict
marketing_campaign_settings_info_from_dict = MarketingCampaignSettingsInfo.from_dict(marketing_campaign_settings_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


