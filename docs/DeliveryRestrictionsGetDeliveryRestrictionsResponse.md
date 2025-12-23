# DeliveryRestrictionsGetDeliveryRestrictionsResponse

Response for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**delivery_restrictions** | [**List[DeliveryRestrictionsDeliveryRestrictions]**](DeliveryRestrictionsDeliveryRestrictions.md) | Delivery restrictions. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_get_delivery_restrictions_response import DeliveryRestrictionsGetDeliveryRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsGetDeliveryRestrictionsResponse from a JSON string
delivery_restrictions_get_delivery_restrictions_response_instance = DeliveryRestrictionsGetDeliveryRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsGetDeliveryRestrictionsResponse.to_json())

# convert the object into a dict
delivery_restrictions_get_delivery_restrictions_response_dict = delivery_restrictions_get_delivery_restrictions_response_instance.to_dict()
# create an instance of DeliveryRestrictionsGetDeliveryRestrictionsResponse from a dict
delivery_restrictions_get_delivery_restrictions_response_from_dict = DeliveryRestrictionsGetDeliveryRestrictionsResponse.from_dict(delivery_restrictions_get_delivery_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


