# DeliveryOrderResponseGuestsInfo

Information about order guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons. | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_guests_info import DeliveryOrderResponseGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseGuestsInfo from a JSON string
delivery_order_response_guests_info_instance = DeliveryOrderResponseGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseGuestsInfo.to_json())

# convert the object into a dict
delivery_order_response_guests_info_dict = delivery_order_response_guests_info_instance.to_dict()
# create an instance of DeliveryOrderResponseGuestsInfo from a dict
delivery_order_response_guests_info_from_dict = DeliveryOrderResponseGuestsInfo.from_dict(delivery_order_response_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


