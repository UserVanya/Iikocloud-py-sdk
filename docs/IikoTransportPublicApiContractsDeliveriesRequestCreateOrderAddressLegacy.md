# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet.md) | Street.  &gt; It&#39;s required specify only \&quot;classifierId\&quot; or \&quot;id\&quot; or \&quot;name\&quot; and \&quot;city\&quot;. | 
**index** | **str** | Postcode. | [optional] 
**house** | **str** | House. | 
**building** | **str** | Building. | [optional] 
**flat** | **str** | Apartment.  &gt; In case useUaeAddressingSystem enabled max length - 100, otherwise - 10. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region_id** | **UUID** | Delivery area ID. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderAddressLegacy.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_address_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


