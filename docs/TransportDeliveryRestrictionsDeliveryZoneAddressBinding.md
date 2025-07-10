# TransportDeliveryRestrictionsDeliveryZoneAddressBinding

Delivery zone polygon, defined by the combination of street, index and house numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_id** | **str** | ID of the delivery zone&#39;s street. | 
**postcode** | **str** | Postcode. | 
**houses** | [**TransportDeliveryRestrictionsHousesRange**](TransportDeliveryRestrictionsHousesRange.md) | Range of house numbers in the delivery zone. | 

## Example

```python
from iiko_cloud_client.models.transport_delivery_restrictions_delivery_zone_address_binding import TransportDeliveryRestrictionsDeliveryZoneAddressBinding

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsDeliveryZoneAddressBinding from a JSON string
transport_delivery_restrictions_delivery_zone_address_binding_instance = TransportDeliveryRestrictionsDeliveryZoneAddressBinding.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsDeliveryZoneAddressBinding.to_json())

# convert the object into a dict
transport_delivery_restrictions_delivery_zone_address_binding_dict = transport_delivery_restrictions_delivery_zone_address_binding_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsDeliveryZoneAddressBinding from a dict
transport_delivery_restrictions_delivery_zone_address_binding_from_dict = TransportDeliveryRestrictionsDeliveryZoneAddressBinding.from_dict(transport_delivery_restrictions_delivery_zone_address_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


