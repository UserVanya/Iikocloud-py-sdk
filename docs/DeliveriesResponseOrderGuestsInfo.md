# DeliveriesResponseOrderGuestsInfo

Information about order guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons. | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_guests_info import DeliveriesResponseOrderGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderGuestsInfo from a JSON string
deliveries_response_order_guests_info_instance = DeliveriesResponseOrderGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderGuestsInfo.to_json())

# convert the object into a dict
deliveries_response_order_guests_info_dict = deliveries_response_order_guests_info_instance.to_dict()
# create an instance of DeliveriesResponseOrderGuestsInfo from a dict
deliveries_response_order_guests_info_from_dict = DeliveriesResponseOrderGuestsInfo.from_dict(deliveries_response_order_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


