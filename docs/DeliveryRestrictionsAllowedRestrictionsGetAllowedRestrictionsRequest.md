# DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

Request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[str]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**delivery_address** | [**DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress**](DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.md) | Delivery address. | [optional] 
**order_location** | [**DeliveryRestrictionsAllowedRestrictionsOrderLocation**](DeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Order location. | [optional] 
**order_items** | [**List[DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem]**](DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.md) | Order list. | [optional] 
**is_courier_delivery** | **bool** | Type of delivery service. | 
**delivery_date** | **str** | Delivery date (Local for delivery terminal). | [optional] 
**delivery_sum** | **float** | Sum. | [optional] 
**discount_sum** | **float** | Discounts sum. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request import DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a JSON string
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance = DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict = delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a dict
delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_from_dict = DeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_dict(delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


