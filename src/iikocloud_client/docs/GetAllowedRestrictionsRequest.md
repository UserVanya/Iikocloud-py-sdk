# GetAllowedRestrictionsRequest

Request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_address** | [**RestrictionsAddress**](RestrictionsAddress.md) | Delivery address. | [optional] 
**delivery_date** | **str** | Delivery date (Local for delivery terminal). | [optional] 
**delivery_sum** | **float** | Sum. | [optional] 
**discount_sum** | **float** | Discounts sum. | [optional] 
**is_courier_delivery** | **bool** | Type of delivery service. | 
**order_items** | [**List[RestrictionsOrderItem]**](RestrictionsOrderItem.md) | Order list. | [optional] 
**order_location** | [**OrderLocation**](OrderLocation.md) | Order location. | [optional] 
**organization_id** | **UUID** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.get_allowed_restrictions_request import GetAllowedRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllowedRestrictionsRequest from a JSON string
get_allowed_restrictions_request_instance = GetAllowedRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllowedRestrictionsRequest.to_json())

# convert the object into a dict
get_allowed_restrictions_request_dict = get_allowed_restrictions_request_instance.to_dict()
# create an instance of GetAllowedRestrictionsRequest from a dict
get_allowed_restrictions_request_from_dict = GetAllowedRestrictionsRequest.from_dict(get_allowed_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


