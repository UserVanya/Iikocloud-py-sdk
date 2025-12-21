# DeliveryRestrictionsDeliveryZone

Delivery zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Polygon name. | 
**coordinates** | [**List[DeliveryRestrictionsCoordinates]**](DeliveryRestrictionsCoordinates.md) | A set of points describing a polygon. | 
**addresses** | [**List[DeliveryRestrictionsDeliveryZoneAddressBinding]**](DeliveryRestrictionsDeliveryZoneAddressBinding.md) | A set of addresses describing a polygon.                &gt; Available only for manual delivery zones. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_delivery_zone import DeliveryRestrictionsDeliveryZone

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsDeliveryZone from a JSON string
delivery_restrictions_delivery_zone_instance = DeliveryRestrictionsDeliveryZone.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsDeliveryZone.to_json())

# convert the object into a dict
delivery_restrictions_delivery_zone_dict = delivery_restrictions_delivery_zone_instance.to_dict()
# create an instance of DeliveryRestrictionsDeliveryZone from a dict
delivery_restrictions_delivery_zone_from_dict = DeliveryRestrictionsDeliveryZone.from_dict(delivery_restrictions_delivery_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


