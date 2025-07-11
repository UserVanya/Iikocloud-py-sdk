# TransportDeliveryRestrictionsDeliveryRestrictionItem

Item of delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_sum** | **float** | The minimum order amount for a given point in a given time interval in this delivery zone. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**zone** | **str** | Name of delivery zone from cartography. | 
**week_map** | **int** | Days of the week. | 
**var_from** | **int** | The time from which the point can process orders from the selected zone, in minutes from the beginning of the day. | 
**to** | **int** | The maximum time at which a point can carry an order to a given zone, in minutes from the beginning of the day. | 
**priority** | **int** | Priority of point in delivery zone. | 
**delivery_duration_in_minutes** | **int** | Delivery duration in delivery zone. | 
**delivery_service_product_id** | **str** | Link to \&quot;delivery service payment\&quot;. | 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_delivery_restriction_item import TransportDeliveryRestrictionsDeliveryRestrictionItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsDeliveryRestrictionItem from a JSON string
transport_delivery_restrictions_delivery_restriction_item_instance = TransportDeliveryRestrictionsDeliveryRestrictionItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsDeliveryRestrictionItem.to_json())

# convert the object into a dict
transport_delivery_restrictions_delivery_restriction_item_dict = transport_delivery_restrictions_delivery_restriction_item_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsDeliveryRestrictionItem from a dict
transport_delivery_restrictions_delivery_restriction_item_from_dict = TransportDeliveryRestrictionsDeliveryRestrictionItem.from_dict(transport_delivery_restrictions_delivery_restriction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


