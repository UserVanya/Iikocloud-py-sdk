# DeliveryOrderResponseAddress

Address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** | Building. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**flat** | **str** | Apartment. | [optional] 
**floor** | **str** | Floor. | [optional] 
**house** | **str** | House. | [optional] 
**index** | **str** | Postcode. | [optional] 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 
**region** | [**DeliveryOrderResponseRegion**](DeliveryOrderResponseRegion.md) | Region | 
**street** | [**DeliveryOrderResponseStreet**](DeliveryOrderResponseStreet.md) | Street. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_address import DeliveryOrderResponseAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseAddress from a JSON string
delivery_order_response_address_instance = DeliveryOrderResponseAddress.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseAddress.to_json())

# convert the object into a dict
delivery_order_response_address_dict = delivery_order_response_address_instance.to_dict()
# create an instance of DeliveryOrderResponseAddress from a dict
delivery_order_response_address_from_dict = DeliveryOrderResponseAddress.from_dict(delivery_order_response_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


