# ReservesGuestsInfo

Reserve guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iikocloud_client.models.reserves_guests_info import ReservesGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesGuestsInfo from a JSON string
reserves_guests_info_instance = ReservesGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(ReservesGuestsInfo.to_json())

# convert the object into a dict
reserves_guests_info_dict = reserves_guests_info_instance.to_dict()
# create an instance of ReservesGuestsInfo from a dict
reserves_guests_info_from_dict = ReservesGuestsInfo.from_dict(reserves_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


