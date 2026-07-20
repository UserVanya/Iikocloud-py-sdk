# DeliveryZoneAddressBinding

Delivery zone polygon, defined by the combination of street, index and house numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**houses** | [**HousesRange**](HousesRange.md) | Range of house numbers in the delivery zone. | 
**postcode** | **str** | Postcode. | 
**street_id** | **UUID** | ID of the delivery zone&#39;s street. | 

## Example

```python
from iikocloud_client.models.delivery_zone_address_binding import DeliveryZoneAddressBinding

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryZoneAddressBinding from a JSON string
delivery_zone_address_binding_instance = DeliveryZoneAddressBinding.from_json(json)
# print the JSON string representation of the object
print(DeliveryZoneAddressBinding.to_json())

# convert the object into a dict
delivery_zone_address_binding_dict = delivery_zone_address_binding_instance.to_dict()
# create an instance of DeliveryZoneAddressBinding from a dict
delivery_zone_address_binding_from_dict = DeliveryZoneAddressBinding.from_dict(delivery_zone_address_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


