# NetCustomerDeleteMagnetCardRequest

Delete magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | 
**card_track** | **str** | Card track. Can be null. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_customer_delete_magnet_card_request import NetCustomerDeleteMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerDeleteMagnetCardRequest from a JSON string
net_customer_delete_magnet_card_request_instance = NetCustomerDeleteMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerDeleteMagnetCardRequest.to_json())

# convert the object into a dict
net_customer_delete_magnet_card_request_dict = net_customer_delete_magnet_card_request_instance.to_dict()
# create an instance of NetCustomerDeleteMagnetCardRequest from a dict
net_customer_delete_magnet_card_request_from_dict = NetCustomerDeleteMagnetCardRequest.from_dict(net_customer_delete_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


