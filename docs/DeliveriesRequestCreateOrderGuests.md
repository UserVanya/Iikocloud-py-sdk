# DeliveriesRequestCreateOrderGuests

Information on guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons in order. This field defines the number of cutlery sets | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_guests import DeliveriesRequestCreateOrderGuests

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderGuests from a JSON string
deliveries_request_create_order_guests_instance = DeliveriesRequestCreateOrderGuests.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderGuests.to_json())

# convert the object into a dict
deliveries_request_create_order_guests_dict = deliveries_request_create_order_guests_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderGuests from a dict
deliveries_request_create_order_guests_from_dict = DeliveriesRequestCreateOrderGuests.from_dict(deliveries_request_create_order_guests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


