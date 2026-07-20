# GuestCardInfo

Guest card info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Card id. | [optional] 
**number** | **str** | Card number. | [optional] 
**track** | **str** | Card track. | [optional] 
**valid_to_date** | **str** | Card valid to date. | [optional] 

## Example

```python
from iikocloud_client.models.guest_card_info import GuestCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestCardInfo from a JSON string
guest_card_info_instance = GuestCardInfo.from_json(json)
# print the JSON string representation of the object
print(GuestCardInfo.to_json())

# convert the object into a dict
guest_card_info_dict = guest_card_info_instance.to_dict()
# create an instance of GuestCardInfo from a dict
guest_card_info_from_dict = GuestCardInfo.from_dict(guest_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


