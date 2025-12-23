# DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

Suitable terminal group with delivery duration and other parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**delivery_duration_in_minutes** | **int** | Delivery duration in minutes. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | 
**delivery_service_product_id** | **str** | Link to \&quot;delivery service payment\&quot;. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_allowed_item_with_duration import DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a JSON string
delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance = DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict = delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a dict
delivery_restrictions_allowed_restrictions_allowed_item_with_duration_from_dict = DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_dict(delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


