# DeliveryRestrictions

Delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_on_validation_rejection** | [**ActionOnValidationRejection**](ActionOnValidationRejection.md) | Action on problems with auto-assignment. | 
**add_delivery_service_cost** | **bool** | Add shipping cost to order. | 
**auto_assign_external_deliveries** | **bool** | Automatically assigned delivery method based on cartography. | 
**default_delivery_duration_in_minutes** | **int** | General standard of delivery time. | 
**default_delivery_service_product_id** | **UUID** | Link to \&quot;delivery service payment\&quot;. | 
**default_from** | **int** | The beginning of the interval of the total work time for all points and delivery zones,   in minutes from the beginning of the day. | 
**default_min_sum** | **float** | Total minimum order amount. | 
**default_self_service_duration_in_minutes** | **int** | Default pickup time. | 
**default_to** | **int** | End of the total work time interval for all points and delivery zones,   in minutes from the beginning of the day. | 
**delivery_geocode_service_type** | [**DeliveryGeocodeServiceType**](DeliveryGeocodeServiceType.md) | Geocoding service type. | 
**delivery_regions_map_url** | **str** | Link to the map of delivery service regions. | 
**delivery_zones** | [**List[DeliveryZone]**](DeliveryZone.md) | Delivery zones. | 
**external_assignation_service_url** | **str** | Address of external delivery distribution service. | 
**front_trusts_call_center_check** | **bool** | Indication whether or not to trust on the fronts the call center mapping restrictions from the call center  if the composition of the order has not changed since the last check. If true, then trust. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reject_on_geocoding_error** | **bool** | Reject delivery if we could not geocode the address. | 
**require_exact_address_for_geocoding** | **bool** | Require an exact geocoding address. | 
**restrictions** | [**List[DeliveryRestrictionItem]**](DeliveryRestrictionItem.md) | Restrictions. | 
**use_external_assignation_service** | **bool** | Use external delivery distribution service. | 
**use_same_delivery_duration** | **bool** | Indication that all delivery points in all delivery zones use common delivery time limits. | 
**use_same_delivery_service_product** | **bool** | Indication that the cost is the same for all points of delivery. | 
**use_same_min_sum** | **bool** | Indication that all delivery points for all delivery zones use the total minimum order amount. | 
**use_same_restrictions_on_all_week** | **bool** | Indication that all delivery points in all zones use the same schedule for all days of the week. | 
**use_same_work_time_interval** | **bool** | Indication that all delivery points in all zones use common time limits. | 
**zones_mode** | [**DeliveryRestrictionsMode**](DeliveryRestrictionsMode.md) | Delivery restrictions mode. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions import DeliveryRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictions from a JSON string
delivery_restrictions_instance = DeliveryRestrictions.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictions.to_json())

# convert the object into a dict
delivery_restrictions_dict = delivery_restrictions_instance.to_dict()
# create an instance of DeliveryRestrictions from a dict
delivery_restrictions_from_dict = DeliveryRestrictions.from_dict(delivery_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


