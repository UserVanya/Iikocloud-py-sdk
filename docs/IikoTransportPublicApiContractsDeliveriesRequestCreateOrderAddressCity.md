# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Address line 1.  Contains the primary address information.   &gt; Allowed from version &#x60;8.7.6&#x60;. | 
**flat** | **str** | Apartment. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region_id** | **UUID** | Delivery area ID. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_address_city import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_address_city_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_address_city_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_address_city_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_address_city_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressCity.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


