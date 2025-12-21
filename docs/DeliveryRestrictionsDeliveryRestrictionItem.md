# DeliveryRestrictionsDeliveryRestrictionItem

Item of delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_sum** | **float** | The minimum order amount for a given point in a given time interval in this delivery zone. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**zone** | **str** | Name of delivery zone from cartography. | 
**week_map** | **int** | Days of the week. | 
**var_from** | **int** | The time from which the point can process orders from the selected zone, in minutes from the beginning of the day. | 
**to** | **int** | The maximum time at which a point can carry an order to a given zone, in minutes from the beginning of the day. | 
**priority** | **int** | Priority of point in delivery zone. | 
**delivery_duration_in_minutes** | **int** | Delivery duration in delivery zone. | 
**delivery_service_product_id** | **UUID** | Link to \&quot;delivery service payment\&quot;. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_delivery_restriction_item import DeliveryRestrictionsDeliveryRestrictionItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsDeliveryRestrictionItem from a JSON string
delivery_restrictions_delivery_restriction_item_instance = DeliveryRestrictionsDeliveryRestrictionItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsDeliveryRestrictionItem.to_json())

# convert the object into a dict
delivery_restrictions_delivery_restriction_item_dict = delivery_restrictions_delivery_restriction_item_instance.to_dict()
# create an instance of DeliveryRestrictionsDeliveryRestrictionItem from a dict
delivery_restrictions_delivery_restriction_item_from_dict = DeliveryRestrictionsDeliveryRestrictionItem.from_dict(delivery_restrictions_delivery_restriction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


