# TransportDeliveriesResponseOrderGuestsInfo

Information about order guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons. | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_guests_info import TransportDeliveriesResponseOrderGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderGuestsInfo from a JSON string
transport_deliveries_response_order_guests_info_instance = TransportDeliveriesResponseOrderGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderGuestsInfo.to_json())

# convert the object into a dict
transport_deliveries_response_order_guests_info_dict = transport_deliveries_response_order_guests_info_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderGuestsInfo from a dict
transport_deliveries_response_order_guests_info_from_dict = TransportDeliveriesResponseOrderGuestsInfo.from_dict(transport_deliveries_response_order_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


