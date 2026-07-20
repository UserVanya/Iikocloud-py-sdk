# GetDeliveryRestrictionsResponse

Response for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**delivery_restrictions** | [**List[DeliveryRestrictions]**](DeliveryRestrictions.md) | Delivery restrictions. | 

## Example

```python
from iikocloud_client.models.get_delivery_restrictions_response import GetDeliveryRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeliveryRestrictionsResponse from a JSON string
get_delivery_restrictions_response_instance = GetDeliveryRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeliveryRestrictionsResponse.to_json())

# convert the object into a dict
get_delivery_restrictions_response_dict = get_delivery_restrictions_response_instance.to_dict()
# create an instance of GetDeliveryRestrictionsResponse from a dict
get_delivery_restrictions_response_from_dict = GetDeliveryRestrictionsResponse.from_dict(get_delivery_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


