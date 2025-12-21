# DeliveryRestrictionsAllowedRestrictionsRejectItemData

Reject additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Point work time start. | [optional] 
**date_to** | **str** | Point work time end. | [optional] 
**allowed_week_days** | **List[str]** | Allowed week days. | [optional] 
**min_sum** | **float** | Order min sum. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_reject_item_data import DeliveryRestrictionsAllowedRestrictionsRejectItemData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsRejectItemData from a JSON string
delivery_restrictions_allowed_restrictions_reject_item_data_instance = DeliveryRestrictionsAllowedRestrictionsRejectItemData.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsRejectItemData.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_reject_item_data_dict = delivery_restrictions_allowed_restrictions_reject_item_data_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsRejectItemData from a dict
delivery_restrictions_allowed_restrictions_reject_item_data_from_dict = DeliveryRestrictionsAllowedRestrictionsRejectItemData.from_dict(delivery_restrictions_allowed_restrictions_reject_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


