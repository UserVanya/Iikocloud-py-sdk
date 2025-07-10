# TransportDeliveryRestrictionsDeliveryZone

Delivery zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Polygon name. | 
**coordinates** | [**List[TransportDeliveryRestrictionsCoordinates]**](TransportDeliveryRestrictionsCoordinates.md) | A set of points describing a polygon. | 
**addresses** | [**List[TransportDeliveryRestrictionsDeliveryZoneAddressBinding]**](TransportDeliveryRestrictionsDeliveryZoneAddressBinding.md) | A set of addresses describing a polygon.                &gt; Available only for manual delivery zones. | 

## Example

```python
from iiko_cloud_client.models.transport_delivery_restrictions_delivery_zone import TransportDeliveryRestrictionsDeliveryZone

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsDeliveryZone from a JSON string
transport_delivery_restrictions_delivery_zone_instance = TransportDeliveryRestrictionsDeliveryZone.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsDeliveryZone.to_json())

# convert the object into a dict
transport_delivery_restrictions_delivery_zone_dict = transport_delivery_restrictions_delivery_zone_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsDeliveryZone from a dict
transport_delivery_restrictions_delivery_zone_from_dict = TransportDeliveryRestrictionsDeliveryZone.from_dict(transport_delivery_restrictions_delivery_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


