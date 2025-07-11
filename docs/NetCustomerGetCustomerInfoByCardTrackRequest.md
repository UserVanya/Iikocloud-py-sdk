# NetCustomerGetCustomerInfoByCardTrackRequest

Request to get customer by card track.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_track** | **str** | Customer card track. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_get_customer_info_by_card_track_request import NetCustomerGetCustomerInfoByCardTrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoByCardTrackRequest from a JSON string
net_customer_get_customer_info_by_card_track_request_instance = NetCustomerGetCustomerInfoByCardTrackRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoByCardTrackRequest.to_json())

# convert the object into a dict
net_customer_get_customer_info_by_card_track_request_dict = net_customer_get_customer_info_by_card_track_request_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoByCardTrackRequest from a dict
net_customer_get_customer_info_by_card_track_request_from_dict = NetCustomerGetCustomerInfoByCardTrackRequest.from_dict(net_customer_get_customer_info_by_card_track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


