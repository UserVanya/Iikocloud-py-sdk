# IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding

Delivery zone polygon, defined by the combination of street, index and house numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_id** | **UUID** | ID of the delivery zone&#39;s street. | 
**postcode** | **str** | Postcode. | 
**houses** | [**IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange**](IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange.md) | Range of house numbers in the delivery zone. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding import IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding_instance = IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding_dict = iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding from a dict
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_address_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


