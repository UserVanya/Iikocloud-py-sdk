# CustomerDeleteMagnetCardRequest

Delete magnet card request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**card_track** | **str** | Card track. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_delete_magnet_card_request import CustomerDeleteMagnetCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDeleteMagnetCardRequest from a JSON string
customer_delete_magnet_card_request_instance = CustomerDeleteMagnetCardRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerDeleteMagnetCardRequest.to_json())

# convert the object into a dict
customer_delete_magnet_card_request_dict = customer_delete_magnet_card_request_instance.to_dict()
# create an instance of CustomerDeleteMagnetCardRequest from a dict
customer_delete_magnet_card_request_from_dict = CustomerDeleteMagnetCardRequest.from_dict(customer_delete_magnet_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


