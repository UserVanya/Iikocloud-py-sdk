# GetAllowedRestrictionsResponse

Response for a request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_external_id** | **str** | Delivery address ID in external mapping system. | 
**allowed_items** | [**List[AllowedItemWithDuration]**](AllowedItemWithDuration.md) | Suitable terminal groups with a delivery duration for them. | 
**correlation_id** | **UUID** | Operation ID. | 
**is_allowed** | **bool** | A sign of successful verification. | 
**location** | [**OrderLocation**](OrderLocation.md) | Coordinates returned by geocoding service. | 
**reject_cause** | **str** | Reject cause. | 
**rejected_items** | [**List[RejectItem]**](RejectItem.md) | Rejected items with cause. | 

## Example

```python
from iikocloud_client.models.get_allowed_restrictions_response import GetAllowedRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllowedRestrictionsResponse from a JSON string
get_allowed_restrictions_response_instance = GetAllowedRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllowedRestrictionsResponse.to_json())

# convert the object into a dict
get_allowed_restrictions_response_dict = get_allowed_restrictions_response_instance.to_dict()
# create an instance of GetAllowedRestrictionsResponse from a dict
get_allowed_restrictions_response_from_dict = GetAllowedRestrictionsResponse.from_dict(get_allowed_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


