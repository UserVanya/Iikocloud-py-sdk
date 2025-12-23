# CustomerGetCustomerInfoByCardTrackRequest

Request to get customer by card track.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_track** | **str** | Customer card track. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_by_card_track_request import CustomerGetCustomerInfoByCardTrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoByCardTrackRequest from a JSON string
customer_get_customer_info_by_card_track_request_instance = CustomerGetCustomerInfoByCardTrackRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoByCardTrackRequest.to_json())

# convert the object into a dict
customer_get_customer_info_by_card_track_request_dict = customer_get_customer_info_by_card_track_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoByCardTrackRequest from a dict
customer_get_customer_info_by_card_track_request_from_dict = CustomerGetCustomerInfoByCardTrackRequest.from_dict(customer_get_customer_info_by_card_track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


