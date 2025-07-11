# TransportReservesGuestsInfo

Reserve guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iikocloud_client.models.transport_reserves_guests_info import TransportReservesGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesGuestsInfo from a JSON string
transport_reserves_guests_info_instance = TransportReservesGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(TransportReservesGuestsInfo.to_json())

# convert the object into a dict
transport_reserves_guests_info_dict = transport_reserves_guests_info_instance.to_dict()
# create an instance of TransportReservesGuestsInfo from a dict
transport_reserves_guests_info_from_dict = TransportReservesGuestsInfo.from_dict(transport_reserves_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


