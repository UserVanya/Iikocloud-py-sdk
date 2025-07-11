# TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

Response for a request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**is_allowed** | **bool** | A sign of successful verification. | 
**reject_cause** | **str** | Reject cause. | 
**address_external_id** | **str** | Delivery address ID in external mapping system. | 
**location** | [**TransportDeliveryRestrictionsAllowedRestrictionsOrderLocation**](TransportDeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Coordinates returned by geocoding service. | 
**allowed_items** | [**List[TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration]**](TransportDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.md) | Suitable terminal groups with a delivery duration for them. | 
**rejected_items** | [**List[TransportDeliveryRestrictionsAllowedRestrictionsRejectItem]**](TransportDeliveryRestrictionsAllowedRestrictionsRejectItem.md) | Rejected items with cause. | 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response import TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a JSON string
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance = TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict = transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a dict
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_dict(transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


