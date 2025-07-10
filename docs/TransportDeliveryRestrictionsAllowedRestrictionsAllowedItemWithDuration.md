# TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

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
from iiko_cloud_client.models.transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration import TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a JSON string
transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance = TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict = transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a dict
transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_dict(transport_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


