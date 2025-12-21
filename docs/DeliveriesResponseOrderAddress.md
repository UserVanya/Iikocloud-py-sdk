# DeliveriesResponseOrderAddress

Address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | [**DeliveriesResponseOrderStreet**](DeliveriesResponseOrderStreet.md) | Street. | [optional] 
**index** | **str** | Postcode. | [optional] 
**house** | **str** | House. | [optional] 
**building** | **str** | Building. | [optional] 
**flat** | **str** | Apartment. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region** | [**DeliveriesResponseOrderRegion**](DeliveriesResponseOrderRegion.md) | Region | 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_address import DeliveriesResponseOrderAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderAddress from a JSON string
deliveries_response_order_address_instance = DeliveriesResponseOrderAddress.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderAddress.to_json())

# convert the object into a dict
deliveries_response_order_address_dict = deliveries_response_order_address_instance.to_dict()
# create an instance of DeliveriesResponseOrderAddress from a dict
deliveries_response_order_address_from_dict = DeliveriesResponseOrderAddress.from_dict(deliveries_response_order_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


