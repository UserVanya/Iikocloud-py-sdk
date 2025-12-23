# DeliveriesRequestCreateOrderAddressCity

Order delivery address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Address line 1.  Contains the primary address information.   &gt; Allowed from version &#x60;8.7.6&#x60;. | 
**flat** | **str** | Apartment. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**floor** | **str** | Floor. | [optional] 
**doorphone** | **str** | Intercom. | [optional] 
**region_id** | **str** | Delivery area ID. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_address_city import DeliveriesRequestCreateOrderAddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderAddressCity from a JSON string
deliveries_request_create_order_address_city_instance = DeliveriesRequestCreateOrderAddressCity.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderAddressCity.to_json())

# convert the object into a dict
deliveries_request_create_order_address_city_dict = deliveries_request_create_order_address_city_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderAddressCity from a dict
deliveries_request_create_order_address_city_from_dict = DeliveriesRequestCreateOrderAddressCity.from_dict(deliveries_request_create_order_address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


