# TransportDeliveriesResponseOrderAddress

Address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**TransportDeliveriesResponseOrderStreet**](TransportDeliveriesResponseOrderStreet.md) | Street. | [optional] 
**index** | **str** | Postcode. | [optional] 
**house** | **str** | House. | [optional] 
**building** | **str** | Building. | [optional] 
**flat** | **str** | Apartment. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region** | [**TransportDeliveriesResponseOrderRegion**](TransportDeliveriesResponseOrderRegion.md) | Region | 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_address import TransportDeliveriesResponseOrderAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderAddress from a JSON string
transport_deliveries_response_order_address_instance = TransportDeliveriesResponseOrderAddress.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderAddress.to_json())

# convert the object into a dict
transport_deliveries_response_order_address_dict = transport_deliveries_response_order_address_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderAddress from a dict
transport_deliveries_response_order_address_from_dict = TransportDeliveriesResponseOrderAddress.from_dict(transport_deliveries_response_order_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


