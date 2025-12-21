# CustomerAddMagnetCardRequest

Add magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**card_track** | **str** | Card track. Can be null. | 
**card_number** | **str** | Card number. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_add_magnet_card_request import CustomerAddMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAddMagnetCardRequest from a JSON string
customer_add_magnet_card_request_instance = CustomerAddMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerAddMagnetCardRequest.to_json())

# convert the object into a dict
customer_add_magnet_card_request_dict = customer_add_magnet_card_request_instance.to_dict()
# create an instance of CustomerAddMagnetCardRequest from a dict
customer_add_magnet_card_request_from_dict = CustomerAddMagnetCardRequest.from_dict(customer_add_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


