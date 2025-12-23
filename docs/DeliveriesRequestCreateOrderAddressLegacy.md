# DeliveriesRequestCreateOrderAddressLegacy

Order delivery legacy address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**DeliveriesRequestCreateOrderStreet**](DeliveriesRequestCreateOrderStreet.md) | Street.  &gt; It&#39;s required specify only \&quot;classifierId\&quot; or \&quot;id\&quot; or \&quot;name\&quot; and \&quot;city\&quot;. | 
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
from iikocloud_client.models.deliveries_request_create_order_address_legacy import DeliveriesRequestCreateOrderAddressLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderAddressLegacy from a JSON string
deliveries_request_create_order_address_legacy_instance = DeliveriesRequestCreateOrderAddressLegacy.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderAddressLegacy.to_json())

# convert the object into a dict
deliveries_request_create_order_address_legacy_dict = deliveries_request_create_order_address_legacy_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderAddressLegacy from a dict
deliveries_request_create_order_address_legacy_from_dict = DeliveriesRequestCreateOrderAddressLegacy.from_dict(deliveries_request_create_order_address_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


