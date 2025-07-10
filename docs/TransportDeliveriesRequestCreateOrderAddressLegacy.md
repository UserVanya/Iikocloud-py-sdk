# TransportDeliveriesRequestCreateOrderAddressLegacy

Order delivery legacy address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**TransportDeliveriesRequestCreateOrderStreet**](TransportDeliveriesRequestCreateOrderStreet.md) | Street.  &gt; It&#39;s required specify only \&quot;classifierId\&quot; or \&quot;id\&quot; or \&quot;name\&quot; and \&quot;city\&quot;. | 
**index** | **str** | Postcode. | [optional] 
**house** | **str** | House. | 
**building** | **str** | Building. | [optional] 
**flat** | **str** | Apartment.  &gt; In case useUaeAddressingSystem enabled max length - 100, otherwise - 10. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region_id** | **str** | Delivery area ID. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_address_legacy import TransportDeliveriesRequestCreateOrderAddressLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderAddressLegacy from a JSON string
transport_deliveries_request_create_order_address_legacy_instance = TransportDeliveriesRequestCreateOrderAddressLegacy.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderAddressLegacy.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_address_legacy_dict = transport_deliveries_request_create_order_address_legacy_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderAddressLegacy from a dict
transport_deliveries_request_create_order_address_legacy_from_dict = TransportDeliveriesRequestCreateOrderAddressLegacy.from_dict(transport_deliveries_request_create_order_address_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


