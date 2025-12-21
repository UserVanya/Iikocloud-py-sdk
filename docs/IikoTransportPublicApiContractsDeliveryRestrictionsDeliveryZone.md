# IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone

Delivery zone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Polygon name. | 
**coordinates** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsCoordinates]**](IikoTransportPublicApiContractsDeliveryRestrictionsCoordinates.md) | A set of points describing a polygon. | 
**addresses** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding]**](IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZoneAddressBinding.md) | A set of addresses describing a polygon.                &gt; Available only for manual delivery zones. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone import IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_instance = IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_dict = iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone from a dict
iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryZone.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_delivery_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


