# DeliveryZone

Delivery zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[DeliveryZoneAddressBinding]**](DeliveryZoneAddressBinding.md) | A set of addresses describing a polygon.                &gt; Available only for manual delivery zones. | 
**coordinates** | [**List[DeliveryRestrictionCoordinates]**](DeliveryRestrictionCoordinates.md) | A set of points describing a polygon. | 
**name** | **str** | Polygon name. | 

## Example

```python
from iikocloud_client.models.delivery_zone import DeliveryZone

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryZone from a JSON string
delivery_zone_instance = DeliveryZone.from_json(json)
# print the JSON string representation of the object
print(DeliveryZone.to_json())

# convert the object into a dict
delivery_zone_dict = delivery_zone_instance.to_dict()
# create an instance of DeliveryZone from a dict
delivery_zone_from_dict = DeliveryZone.from_dict(delivery_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


