# DeliveryRestrictionsAllowedRestrictionsRejectItem

Rejected item info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | [optional] 
**reject_code** | [**DeliveryRestrictionsAllowedRestrictionsDeliveryRestrictionRejectCode**](DeliveryRestrictionsAllowedRestrictionsDeliveryRestrictionRejectCode.md) | Reject cause code. | 
**reject_hint** | **str** | Reject hint. | 
**reject_item_data** | [**DeliveryRestrictionsAllowedRestrictionsRejectItemData**](DeliveryRestrictionsAllowedRestrictionsRejectItemData.md) | Reject additional information. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_reject_item import DeliveryRestrictionsAllowedRestrictionsRejectItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsRejectItem from a JSON string
delivery_restrictions_allowed_restrictions_reject_item_instance = DeliveryRestrictionsAllowedRestrictionsRejectItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsRejectItem.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_reject_item_dict = delivery_restrictions_allowed_restrictions_reject_item_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsRejectItem from a dict
delivery_restrictions_allowed_restrictions_reject_item_from_dict = DeliveryRestrictionsAllowedRestrictionsRejectItem.from_dict(delivery_restrictions_allowed_restrictions_reject_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


