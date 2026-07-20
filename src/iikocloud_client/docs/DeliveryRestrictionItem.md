# DeliveryRestrictionItem

Item of delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_duration_in_minutes** | **int** | Delivery duration in delivery zone. | 
**delivery_service_product_id** | **UUID** | Link to \&quot;delivery service payment\&quot;. | 
**var_from** | **int** | The time from which the point can process orders from the selected zone, in minutes from the beginning of the day. | 
**min_sum** | **float** | The minimum order amount for a given point in a given time interval in this delivery zone. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**priority** | **int** | Priority of point in delivery zone. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**to** | **int** | The maximum time at which a point can carry an order to a given zone, in minutes from the beginning of the day. | 
**week_map** | **int** | Days of the week. | 
**zone** | **str** | Name of delivery zone from cartography. | 

## Example

```python
from iikocloud_client.models.delivery_restriction_item import DeliveryRestrictionItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionItem from a JSON string
delivery_restriction_item_instance = DeliveryRestrictionItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionItem.to_json())

# convert the object into a dict
delivery_restriction_item_dict = delivery_restriction_item_instance.to_dict()
# create an instance of DeliveryRestrictionItem from a dict
delivery_restriction_item_from_dict = DeliveryRestrictionItem.from_dict(delivery_restriction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


