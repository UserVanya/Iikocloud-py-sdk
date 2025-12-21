# IikoTransportPublicApiContractsDeliveriesResponseOrderAddress

Address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderStreet**](IikoTransportPublicApiContractsDeliveriesResponseOrderStreet.md) | Street. | [optional] 
**index** | **str** | Postcode. | [optional] 
**house** | **str** | House. | [optional] 
**building** | **str** | Building. | [optional] 
**flat** | **str** | Apartment. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderRegion**](IikoTransportPublicApiContractsDeliveriesResponseOrderRegion.md) | Region | 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_address import IikoTransportPublicApiContractsDeliveriesResponseOrderAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderAddress from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_address_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderAddress.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderAddress.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_address_dict = iiko_transport_public_api_contracts_deliveries_response_order_address_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderAddress from a dict
iiko_transport_public_api_contracts_deliveries_response_order_address_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderAddress.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


