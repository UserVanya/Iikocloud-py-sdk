# ReserveGuestsInfo

Reserve guests information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Guests count. | 

## Example

```python
from iikocloud_client.models.reserve_guests_info import ReserveGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveGuestsInfo from a JSON string
reserve_guests_info_instance = ReserveGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(ReserveGuestsInfo.to_json())

# convert the object into a dict
reserve_guests_info_dict = reserve_guests_info_instance.to_dict()
# create an instance of ReserveGuestsInfo from a dict
reserve_guests_info_from_dict = ReserveGuestsInfo.from_dict(reserve_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


