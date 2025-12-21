# DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

Response for a request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_allowed** | **bool** | A sign of successful verification. | 
**reject_cause** | **str** | Reject cause. | 
**address_external_id** | **str** | Delivery address ID in external mapping system. | 
**location** | [**DeliveryRestrictionsAllowedRestrictionsOrderLocation**](DeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Coordinates returned by geocoding service. | 
**allowed_items** | [**List[DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration]**](DeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.md) | Suitable terminal groups with a delivery duration for them. | 
**rejected_items** | [**List[DeliveryRestrictionsAllowedRestrictionsRejectItem]**](DeliveryRestrictionsAllowedRestrictionsRejectItem.md) | Rejected items with cause. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response import DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a JSON string
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance = DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict = delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a dict
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_from_dict = DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_dict(delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


