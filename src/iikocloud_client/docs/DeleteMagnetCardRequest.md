# DeleteMagnetCardRequest

Delete magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_track** | **str** | Card track. Can be null. | 
**customer_id** | **UUID** | Customer id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.delete_magnet_card_request import DeleteMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMagnetCardRequest from a JSON string
delete_magnet_card_request_instance = DeleteMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteMagnetCardRequest.to_json())

# convert the object into a dict
delete_magnet_card_request_dict = delete_magnet_card_request_instance.to_dict()
# create an instance of DeleteMagnetCardRequest from a dict
delete_magnet_card_request_from_dict = DeleteMagnetCardRequest.from_dict(delete_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


