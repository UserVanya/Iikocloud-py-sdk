# AddMagnetCardRequest

Add magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Card number. Can be null. | 
**card_track** | **str** | Card track. Can be null. | 
**customer_id** | **UUID** | Customer id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.add_magnet_card_request import AddMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddMagnetCardRequest from a JSON string
add_magnet_card_request_instance = AddMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(AddMagnetCardRequest.to_json())

# convert the object into a dict
add_magnet_card_request_dict = add_magnet_card_request_instance.to_dict()
# create an instance of AddMagnetCardRequest from a dict
add_magnet_card_request_from_dict = AddMagnetCardRequest.from_dict(add_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


