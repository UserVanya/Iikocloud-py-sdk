# TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse

Response for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**delivery_restrictions** | [**List[TransportDeliveryRestrictionsDeliveryRestrictions]**](TransportDeliveryRestrictionsDeliveryRestrictions.md) | Delivery restrictions. | 

## Example

```python
from iiko_cloud_client.models.transport_delivery_restrictions_get_delivery_restrictions_response import TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse from a JSON string
transport_delivery_restrictions_get_delivery_restrictions_response_instance = TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse.to_json())

# convert the object into a dict
transport_delivery_restrictions_get_delivery_restrictions_response_dict = transport_delivery_restrictions_get_delivery_restrictions_response_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse from a dict
transport_delivery_restrictions_get_delivery_restrictions_response_from_dict = TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse.from_dict(transport_delivery_restrictions_get_delivery_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


