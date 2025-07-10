# NetCustomerAddMagnetCardRequest

Add magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | 
**card_track** | **str** | Card track. Can be null. | 
**card_number** | **str** | Card number. Can be null. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_customer_add_magnet_card_request import NetCustomerAddMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerAddMagnetCardRequest from a JSON string
net_customer_add_magnet_card_request_instance = NetCustomerAddMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerAddMagnetCardRequest.to_json())

# convert the object into a dict
net_customer_add_magnet_card_request_dict = net_customer_add_magnet_card_request_instance.to_dict()
# create an instance of NetCustomerAddMagnetCardRequest from a dict
net_customer_add_magnet_card_request_from_dict = NetCustomerAddMagnetCardRequest.from_dict(net_customer_add_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


