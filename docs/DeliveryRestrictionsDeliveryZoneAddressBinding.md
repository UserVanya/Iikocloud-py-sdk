# DeliveryRestrictionsDeliveryZoneAddressBinding

Delivery zone polygon, defined by the combination of street, index and house numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_id** | **UUID** | ID of the delivery zone&#39;s street. | 
**postcode** | **str** | Postcode. | 
**houses** | [**DeliveryRestrictionsHousesRange**](DeliveryRestrictionsHousesRange.md) | Range of house numbers in the delivery zone. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_delivery_zone_address_binding import DeliveryRestrictionsDeliveryZoneAddressBinding

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsDeliveryZoneAddressBinding from a JSON string
delivery_restrictions_delivery_zone_address_binding_instance = DeliveryRestrictionsDeliveryZoneAddressBinding.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsDeliveryZoneAddressBinding.to_json())

# convert the object into a dict
delivery_restrictions_delivery_zone_address_binding_dict = delivery_restrictions_delivery_zone_address_binding_instance.to_dict()
# create an instance of DeliveryRestrictionsDeliveryZoneAddressBinding from a dict
delivery_restrictions_delivery_zone_address_binding_from_dict = DeliveryRestrictionsDeliveryZoneAddressBinding.from_dict(delivery_restrictions_delivery_zone_address_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


