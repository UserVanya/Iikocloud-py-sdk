# TransportDeliveriesRequestCreateOrderGuests

Information on guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons in order. This field defines the number of cutlery sets | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_guests import TransportDeliveriesRequestCreateOrderGuests

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderGuests from a JSON string
transport_deliveries_request_create_order_guests_instance = TransportDeliveriesRequestCreateOrderGuests.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderGuests.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_guests_dict = transport_deliveries_request_create_order_guests_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderGuests from a dict
transport_deliveries_request_create_order_guests_from_dict = TransportDeliveriesRequestCreateOrderGuests.from_dict(transport_deliveries_request_create_order_guests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


